#!/usr/bin/node
const request = require('request');
const API_URL = 'https://swapi-api.hbtn.io/api';

if (process.argv.length > 2) {
  request(`${API_URL}/films/${process.argv[2]}/`, (error, _, body) => {
    if (error) {
      console.log(error);
    }
    const charURL = JSON.parse(body).characters;
    const charName = charURL.map(
      url => new Promise((resolve, reject) => {
        request(url, (promiseError, __, charReqBody) => {
          if (promiseError) {
            reject(promiseError);
          }
          resolve(JSON.parse(charReqBody).name);
        });
      }));

    Promise.all(charName)
      .then(names => console.log(names.join('\n')))
      .catch(allErrors => console.log(allErrors));
  });
}
