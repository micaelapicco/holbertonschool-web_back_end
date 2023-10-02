function handleResponseFromAPI(promise) {
  return promise
    /*eslint-disable*/
    .then((data) => {
      console.log('Got a response from the API');
      return {
        stauts: 200,
        body: 'success',
      };
    })
    .catch((error) => {
      console.log('Got a response from the API');
      return new Error();
    });
}
export default handleResponseFromAPI;
