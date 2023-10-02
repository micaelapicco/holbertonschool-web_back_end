function handleResponseFromAPI(promise) {
  return promise
    /*eslint-disable*/
    .then((data) => {
    /* eslint-enable */
      console.log('Got a response from the API');
      return {
        body: 'success',
        status: 200,
      };
    })
    /*eslint-disable*/
    .catch((error) => {
    /* eslint-enable */
      console.log('Got a response from the API');
      throw new Error();
    });
}
export default handleResponseFromAPI;
