const sdk = require('api')('@upbit/v1.3.4#1h2zv2al3jq48nm');

sdk.({isDetails: 'false'})
    .then(({ data }) => console.log(data))
    .catch(err => console.error(err));