import axios, { AxiosResponse } from 'axios';
import { API_ROOT } from "../config";

export const moveTankReverse = (): Promise<AxiosResponse<void>> => {
    return axios.post(API_ROOT + '/tank/reverse');
}