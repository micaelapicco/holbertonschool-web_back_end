import { uploadPhoto, createUser } from './utils';

function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
    .then(([photo, user]) => {
      console.log(`${photo.body} ${user.firstName} ${user.lastName}`);
    })
    /*eslint-disable*/
    .catch((error) => {
      console.log('Signup system offline');
      return new Error();
    });
}
export default handleProfileSignup;
