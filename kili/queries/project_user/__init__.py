from ...helpers import deprecate, format_result, fragment_builder
from .queries import gql_project_users
from ...types import ProjectUser
import warnings


class QueriesProjectUser:

    def __init__(self, auth):
        """
        Initializes the subclass

        Parameters
        ----------
        - auth : KiliAuth object
        """
        self.auth = auth

    @deprecate(
        """
        **New feature has been added : Query only the fields you want
        using the field argument, that accept a list of string organized like below.**
        The former default query with all fields is deprecated since 13/05/2020
        After 13/06/2020, the default queried fields will be :
        ['id', 'activated', 'role', 'user.id', 'user.email', 'user.name', 'starred']
        To fetch more fields, for example the kpis fields, just add those :
        fields = ['activated', 'id', 'consensusMark', 'honeypotMark', 'lastLabelingAt', 
        'numberOfAnnotations', 'numberOfLabeledAssets','numberOfLabels', 'role', 'starred', 
        'totalDuration', 'user.id', 'user.email', 'user.name']
        """)
    def project_users(self, email=None, id=None, organization_id=None, project_id=None, fields=None, first=100, skip=0, with_kpis=False):
        """
        Return projects and their users (possibly with their KPIs)

        Parameters
        ----------
        - email : str, optional (default = None)
        - organization_id : str, optional (default = None)
        - project_id : str, optional (default = None)
        - fields : list, optional (default = None)
            All the fields to request among the possible fields for the projectUsers, default for None are the non-calculated fields)
            - Possible fields : see https://cloud.kili-technology.com/docs/python-graphql-api/graphql-api/#projectuser
            - Default fields : `['id', 'activated', 'role', 'user.id', 'user.email', 'user.name', 'starred']`
        - first : int, optional (default = 100)
            Maximum number of users to return
        - skip : int, optional (default = 0)
            Number of project users to skip
        - with_kpis : bool, optional (default = False)
            Whether or not to compute kpis

        Returns
        -------
        - a result object which contains the query if it was successful, or an error message else.
        """
        if not fields:
            fields = ['activated', 'id', 'consensusMark', 'honeypotMark', 'lastLabelingAt', 'numberOfAnnotations', 'numberOfLabeledAssets',
                      'numberOfLabels', 'role', 'starred', 'totalDuration', 'user.id', 'user.email', 'user.name'] if with_kpis else ['id', 'activated', 'role', 'user.id', 'user.email', 'user.name', 'starred']
        variables = {
            'first': first,
            'skip': skip,
            'where': {
                'id': id,
                'project': {
                    'id': project_id,
                },
                'user': {
                    'email': email,
                    'organization': {
                        'id': organization_id,
                    }
                },
            }
        }
        GQL_PROJECT_USERS = gql_project_users(
            fragment_builder(fields, ProjectUser))
        result = self.auth.client.execute(GQL_PROJECT_USERS, variables)
        return format_result('data', result)
