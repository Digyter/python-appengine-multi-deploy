from propertylib import Properties
from django.views.generic.base import TemplateView
import json
class Main(TemplateView):

  def get(
      self,
      request,
      *unused_args,
      **unused_kwargs):
    """Renders main page.

    Args:
      request: An Http request object.
      *unused_args: n/a.
      **kwargs: Contains keyword arg to get the entity.

    Returns:
      An HTTP Response object with the main page.
    """

    self.template_name = 'app/index.html'
    properties = Properties().get()
    context = {
    	'appname': properties['APP_NAME'],
    	'properties': json.dumps(Properties().get())}
    return self.render_to_response(context)