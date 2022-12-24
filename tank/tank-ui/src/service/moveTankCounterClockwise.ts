import axios, { AxiosResponse } from 'axios';
import { API_ROOT } from "../config";

export const moveTankCounterClockwise = (): Promise<AxiosResponse<void>> => {
    return axios.post(API_ROOT + '/tank/counter-clockwise');
}