function getResponseFromAPI() {
  return new Promise((resolve, reject) => {
    const responseData = { message: 'responsee' };
    resolve(responseData);
    if (reject) {
      console.log(reject);
    }
  });
}
export default getResponseFromAPI;
