'''
Why middleware required -
middleware is used for to perform some operation or getting some value each and evey views and templates
we have to use middleware

for example - getting user is admin or not
We can check user is admin or not using request.user.is_staff  but this line we have to again and again when it
will return inside the template then query will get fire
so better to store this value to request/session using middleware before request porocess to views


one more example you want to use some views by only admin then for checking user is admin or not we have to check again and again
then here better to write middle before request coming to view

midlleware sequence execute based on top to bottom for request
and bottom to top for response

'''

class AdminMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response

        #one-time configuration and initialization

    def __call__(self, request):

        '''
        Code to be executed for each request before
        the view (and later middleware) are called
        '''

        response = self.get_response(request)
        '''
        Code to be for each request/response after the 
        view is called
        '''

        return response


    def process_view(self,request, view_func, *view_args, **view_kargs):
        '''
        called just before Django calls the view
        Return either none or HttpResponse
        '''
        request.admin_status = None
        if request.user.is_authenticated:
            request.admin_status = request.user.is_staff

    def process_exception(self,request,exception):
        '''
        called for the response if exception is raised by view.
        Return either none or HttpResponse
        '''
        pass

    def process_template_response(self,request,response):
        '''
        request - HttoRequest object.
        response - TemplateResponse object

        return templateresponse
        use this for changing template or context if it is needed.
        '''
        pass


'''
For Testing I am writing print("Admin User") if request.admin_status else print("Not Admin User")
in every Views

Tested in User login user
Tested in My Address View called due to click on MyProfile

'''
