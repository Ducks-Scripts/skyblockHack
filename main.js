let myAsyncFunction = async () => {
    let response = await fetch("https://api.hypixel.net/key");
    let data = await response.json;
    console.log(data);
    return data;
  };