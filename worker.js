export default {
    async fetch(request, env, ctx) {
      const url = new URL(request.url);
      const params = new URLSearchParams(url.search);
      const targetUrl = params.get('url')
      const method = url.searchParams.get('method') || 'GET';
      const headers = url.searchParams.get('headers');
      const data = url.searchParams.get('data');
      const cookies = url.searchParams.get('cookies');
  
      const requestInit = {
        method,
        headers: headers ? JSON.parse(headers) : {},
        body: data ? JSON.parse(data) : null,
        cookies: cookies ? JSON.parse(cookies) : {}
      };
      console.log(targetUrl);
      console.log(method);
      console.log(headers);
      console.log(data);
      console.log(cookies);
      if(!targetUrl){
        return new Response("None");
      }
      const response = await fetch(targetUrl, requestInit);
      return response;
    },
  };