"use server";
export default class UserManager {
  base_url: string;
  constructor() {
    this.base_url =
      "https://wnscghtuqzqlnlmthgpyhzdmby0cbgps.lambda-url.us-east-1.on.aws";
  }

  async createUser(
    username: string,
    registered_device_id: string,
    personal_contact: BigInteger,
    country: string
  ) {
    let url = `${this.base_url}/user/new?name=${username}&registered_device_id=${registered_device_id}&personal_contact=${personal_contact}&country=${country}`;

    const currentHeaders = new Headers();
    currentHeaders.append("Accept", "application/json");
    currentHeaders.append("Access-Control-Allow-Origin", "*");

    const requestOptions = {
      method: "POST",
      headers: currentHeaders,
    };

    return fetch(url, requestOptions)
      .then(async (i) => {
        let results = JSON.parse(await i.text());
        console.log(await results);
        return await results.id;
      })
      .then((id) => {
        return id;
      });
  }

  async checkIfUserExists(user_details : any) {
    console.log(user_details);
    return import.meta.env.VITE_TRUTHY_VALUE;
  }
}
