
import url from '../config/request';

export default function getQuestion(alreadyFeatures, params, answers) {
  return new Promise(async (next, reject) => {
    let body

    if(alreadyFeatures.length)
      body = JSON.stringify({ alreadyFeatures, params, answers });
    else
      body = JSON.stringify({});

    try {
      const call = await fetch(`${url}/api/questions/`, {
        method: 'POST',
        headers: {
          'content-type': 'application/json'
        },
        body
      });

      const res = await call.json();

      next(res);
    } catch(error) {
      console.log(error);
      reject('Error on get Question');
    }
  });
}