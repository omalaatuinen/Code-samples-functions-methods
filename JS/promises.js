//long example with promises
const p = new Promise((resolve, reject)=>{
  setTimeout(()=>{
      console.log('Doing something, for example, requesting something');
      const someData = {
          prop1: 'val1',
          prop2: 'val2'
      }
      resolve(someData);
  }, 2000);
})
p.then(data=>{
  return new Promise((resolve, reject)=>{
      setTimeout(()=>{
          data.modified=true;
          console.log(data);
          resolve(data);
      }, 1500);
  })
})
.then(clientData=>{
  clientData.fromPromise = true;
  console.log(clientData);
  return clientData;
})
.then(data=>{
  console.log('modified', data);
});

// short example with promise in function

const sleep = ms => new Promise(resolve => setTimeout(()=> resolve(), ms)); //Function declaration

// And now, using this function:
sleep(2000).then(()=> console.log('Aft.2 secs'));

