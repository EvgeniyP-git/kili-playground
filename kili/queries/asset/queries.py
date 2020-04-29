from .fragments import ASSET_FRAGMENT

GQL_GET_ASSET = f'''
query($assetID: ID!) {{
  data: getAsset(assetID: $assetID) {{
    {ASSET_FRAGMENT}
  }}
}}
'''


def GQL_ASSETS(fragment):
    return f'''
query($where: AssetWhere!, $first: PageSize!, $skip: Int!) {{
  data: assets(where: $where, skip: $skip, first: $first) {{
    {fragment}
  }}
}}
'''


GQL_GET_NEXT_ASSET_FROM_LABEL = f'''
query($labelAssetIDs: [ID!]) {{
  data: getNextAssetFromLabel(labelAssetIDs: $labelAssetIDs, where: {{}}) {{
    {ASSET_FRAGMENT}
  }}
}}
'''

GQL_GET_NEXT_ASSET_FROM_PROJECT = f'''
query($projectID: ID!) {{
  data: getNextAssetFromProject(projectID: $projectID) {{
    {ASSET_FRAGMENT}
  }}
}}
'''

GQL_ASSETS_COUNT = f'''
query($where: AssetWhere!) {{
  data: countAssets(where: $where)
}}
'''
