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
    return this.apiClient.get(`/vehicle_data/`, {
      params: { size: 30 } }
    ).then(({data}) => {
      return data;
    });
  }

  getVehicleDataByID(vehicle_id, start="", end="", pageNumber=0 ) {
    const params = { size: 30 }
    if (start != ""){ params['start'] = start}
    if (end != ""){ params['end'] = end}
    if (pageNumber != 0){ params['page'] = pageNumber}

    return this.apiClient.get(`/vehicle_data/${vehicle_id}`, {
      params: params
    }).then(({data}) => {
      return data;
    });
  }

  exportVehicleData(vehicle_id = "", start="", end=""){
    const params = {}
    if (vehicle_id != ""){ params['vehicle_id'] = vehicle_id}
    if (start != ""){ params['start'] = start}
    if (end != ""){ params['end'] = end}

    return this.apiClient.get(`/vehicle_data/write/`, {
      params: params
    }).then(({data}) => {
      return data;
    });
  }

}

export default FastAPIClient;
