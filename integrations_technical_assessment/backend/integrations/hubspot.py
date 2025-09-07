# hubspot.py

import json
import secrets
from fastapi import Request, HTTPException
from fastapi.responses import HTMLResponse
import httpx
import asyncio
import base64
import requests
from integrations.integration_item import IntegrationItem

from redis_client import add_key_value_redis, get_value_redis, delete_key_redis

import os
from dotenv import load_dotenv

load_dotenv()

# Use private access token instead of OAuth2
PRIVATE_ACCESS_TOKEN = os.getenv('HUBSPOT_PRIVATE_ACCESS_TOKEN', 'pat-na2-e2ae00f7-1a80-41f5-ba2a-55b2f5d8d441')

async def authorize_hubspot(user_id, org_id):
    # For private token, we don't need OAuth2 flow - just return mock credentials
    credentials = {
        'access_token': PRIVATE_ACCESS_TOKEN,
        'token_type': 'bearer'
    }
    
    # Store the credentials directly
    await add_key_value_redis(f'hubspot_credentials:{org_id}:{user_id}', json.dumps(credentials), expire=600)
    
    # Return a success indicator instead of auth URL
    return {'status': 'connected', 'message': 'HubSpot connected successfully'}

async def oauth2callback_hubspot(request: Request):
    # Not needed for private token approach, but keeping for API compatibility
    return HTMLResponse(content="<html><script>window.close();</script></html>")

async def get_hubspot_credentials(user_id, org_id):
    credentials = await get_value_redis(f'hubspot_credentials:{org_id}:{user_id}')
    if not credentials:
        # If no stored credentials, create them with the private token
        credentials = {
            'access_token': PRIVATE_ACCESS_TOKEN,
            'token_type': 'bearer'
        }
        await add_key_value_redis(f'hubspot_credentials:{org_id}:{user_id}', json.dumps(credentials), expire=600)
        return credentials
    
    credentials = json.loads(credentials)
    await delete_key_redis(f'hubspot_credentials:{org_id}:{user_id}')
    return credentials

def create_integration_item_metadata_object(
    response_json: dict, item_type: str, parent_id=None, parent_name=None
) -> IntegrationItem:
    integration_item_metadata = IntegrationItem(
        id=str(response_json.get('id', None)) + '_' + item_type,
        name=response_json.get('properties', {}).get('name', response_json.get('properties', {}).get('firstname', 'Unknown')),
        type=item_type,
        parent_id=parent_id,
        parent_path_or_name=parent_name,
        creation_time=response_json.get('createdAt', None),
        last_modified_time=response_json.get('updatedAt', None),
    )

    return integration_item_metadata

def fetch_items(
    access_token: str, url: str, aggregated_response: list, after=None
) -> None:
    """Fetching items from HubSpot API with pagination"""
    params = {'after': after} if after is not None else {}
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        results = data.get('results', [])
        after = data.get('paging', {}).get('next', {}).get('after', None)

        for item in results:
            aggregated_response.append(item)

        if after is not None:
            fetch_items(access_token, url, aggregated_response, after)
    else:
        print(f"Error fetching from {url}: {response.status_code} - {response.text}")

async def get_items_hubspot(credentials) -> list[IntegrationItem]:
    credentials = json.loads(credentials)
    access_token = credentials.get('access_token')
    list_of_integration_item_metadata = []
    
    # HubSpot API endpoints for different object types
    endpoints = {
        'Contact': 'https://api.hubapi.com/crm/v3/objects/contacts',
        'Company': 'https://api.hubapi.com/crm/v3/objects/companies',
        'Deal': 'https://api.hubapi.com/crm/v3/objects/deals'
    }

    for object_type, url in endpoints.items():
        list_of_responses = []
        fetch_items(access_token, url, list_of_responses)
        
        for response in list_of_responses[:10]:  # Limit to first 10 items per type for demo
            list_of_integration_item_metadata.append(
                create_integration_item_metadata_object(response, object_type)
            )

    print(f'list_of_integration_item_metadata: {list_of_integration_item_metadata}')
    return list_of_integration_item_metadata
