import config from './config';

const axios = require('axios');


class FastAPIClient {
  constructor(overrides) {
    this.config = {
      ...config,
      ...overrides,
    };
    this.apiClient = this.getApiClient(this.config);
  }

  /* ----- Client Configuration ----- */
  /* Create Axios client instance pointing at the REST api backend */
  getApiClient(config) {
    const initialConfig = {
      baseURL: `${config.apiBasePath}/api/v1`,
    };
    const client = axios.create(initialConfig);
    return client;
  }

  getVehicleData() {
    return this.apiClient.get(`/vehicle_data/`).then(({data}) => {
      return data;
    });
  }

  getVehicleDataByID(vehicle_id, start="", end="" ) {
    if (start == "" && end == ""){
      return this.apiClient.get(`/vehicle_data/${vehicle_id}`).then(({data}) => {
        return data;
      });
    }
    return this.apiClient.get(`/vehicle_data/${vehicle_id}`, {
      params: {
        start: start,
        end: end
      }
    }).then(({data}) => {
      return data;
    });
  }
}

export default FastAPIClient;
