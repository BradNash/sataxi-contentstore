/**
 * Content Store Rest Service
 * No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)
 *
 * OpenAPI spec version: 1.0
 * 
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 *//* tslint:disable:no-unused-variable member-ordering */

import { Inject, Injectable, Optional }                      from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams,
         HttpResponse, HttpEvent }                           from '@angular/common/http';
import { CustomHttpUrlEncodingCodec }                        from '../encoder';

import { Observable }                                        from 'rxjs';

import { CorrespondenceEventResponse } from '../model/correspondenceEventResponse';
import { FailedResponse } from '../model/failedResponse';
import { SMSTemplateResponse } from '../model/sMSTemplateResponse';

import { BASE_PATH, COLLECTION_FORMATS }                     from '../variables';
import { Configuration }                                     from '../configuration';


@Injectable()
export class CorrespondenceService {

    protected basePath = '%s';
    public defaultHeaders = new HttpHeaders();
    public configuration = new Configuration();

    constructor(protected httpClient: HttpClient, @Optional()@Inject(BASE_PATH) basePath: string, @Optional() configuration: Configuration) {
        if (basePath) {
            this.basePath = basePath;
        }
        if (configuration) {
            this.configuration = configuration;
            this.basePath = basePath || configuration.basePath || this.basePath;
        }
    }

    /**
     * @param consumes string[] mime-types
     * @return true: consumes contains 'multipart/form-data', false: otherwise
     */
    private canConsumeForm(consumes: string[]): boolean {
        const form = 'multipart/form-data';
        for (const consume of consumes) {
            if (form === consume) {
                return true;
            }
        }
        return false;
    }


    /**
     * 
     * This endpoint fetches the correspondence template and populates it with the sms request field values
     * @param templateParameters The parameters required by the template
     * @param identifier The ID of the template to populate
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public correspondenceGetTemplateGet(templateParameters: any, identifier: string, observe?: 'body', reportProgress?: boolean): Observable<SMSTemplateResponse>;
    public correspondenceGetTemplateGet(templateParameters: any, identifier: string, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<SMSTemplateResponse>>;
    public correspondenceGetTemplateGet(templateParameters: any, identifier: string, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<SMSTemplateResponse>>;
    public correspondenceGetTemplateGet(templateParameters: any, identifier: string, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {

        if (templateParameters === null || templateParameters === undefined) {
            throw new Error('Required parameter templateParameters was null or undefined when calling correspondenceGetTemplateGet.');
        }

        if (identifier === null || identifier === undefined) {
            throw new Error('Required parameter identifier was null or undefined when calling correspondenceGetTemplateGet.');
        }

        let queryParameters = new HttpParams({encoder: new CustomHttpUrlEncodingCodec()});
        if (templateParameters !== undefined && templateParameters !== null) {
            queryParameters = queryParameters.set('template_parameters', <any>templateParameters);
        }
        if (identifier !== undefined && identifier !== null) {
            queryParameters = queryParameters.set('identifier', <any>identifier);
        }

        let headers = this.defaultHeaders;

        // authentication (OAuth2) required
        if (this.configuration.accessToken) {
            const accessToken = typeof this.configuration.accessToken === 'function'
                ? this.configuration.accessToken()
                : this.configuration.accessToken;
            headers = headers.set('Authorization', 'Bearer ' + accessToken);
        }

        // to determine the Accept header
        let httpHeaderAccepts: string[] = [
            'application/json'
        ];
        const httpHeaderAcceptSelected: string | undefined = this.configuration.selectHeaderAccept(httpHeaderAccepts);
        if (httpHeaderAcceptSelected != undefined) {
            headers = headers.set('Accept', httpHeaderAcceptSelected);
        }

        // to determine the Content-Type header
        const consumes: string[] = [
        ];

        return this.httpClient.request<SMSTemplateResponse>('get',`${this.basePath}/correspondence/get_template/`,
            {
                params: queryParameters,
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

    /**
     * 
     * This endpoint is using Correspondence Event Type to fetch the list of Correspondence Events
     * @param templateParameters The parameters required by the template
     * @param destination The destination to send to correspondence to, ie &#x27;+2782123456&#x27; or &#x27;johnny.b@goode.com&#x27;
     * @param identifier The ID of the template to populate
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public correspondenceSendCorrespondencePost(templateParameters: any, destination: string, identifier: string, observe?: 'body', reportProgress?: boolean): Observable<CorrespondenceEventResponse>;
    public correspondenceSendCorrespondencePost(templateParameters: any, destination: string, identifier: string, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<CorrespondenceEventResponse>>;
    public correspondenceSendCorrespondencePost(templateParameters: any, destination: string, identifier: string, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<CorrespondenceEventResponse>>;
    public correspondenceSendCorrespondencePost(templateParameters: any, destination: string, identifier: string, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {

        if (templateParameters === null || templateParameters === undefined) {
            throw new Error('Required parameter templateParameters was null or undefined when calling correspondenceSendCorrespondencePost.');
        }

        if (destination === null || destination === undefined) {
            throw new Error('Required parameter destination was null or undefined when calling correspondenceSendCorrespondencePost.');
        }

        if (identifier === null || identifier === undefined) {
            throw new Error('Required parameter identifier was null or undefined when calling correspondenceSendCorrespondencePost.');
        }

        let queryParameters = new HttpParams({encoder: new CustomHttpUrlEncodingCodec()});
        if (templateParameters !== undefined && templateParameters !== null) {
            queryParameters = queryParameters.set('template_parameters', <any>templateParameters);
        }
        if (destination !== undefined && destination !== null) {
            queryParameters = queryParameters.set('destination', <any>destination);
        }
        if (identifier !== undefined && identifier !== null) {
            queryParameters = queryParameters.set('identifier', <any>identifier);
        }

        let headers = this.defaultHeaders;

        // authentication (OAuth2) required
        if (this.configuration.accessToken) {
            const accessToken = typeof this.configuration.accessToken === 'function'
                ? this.configuration.accessToken()
                : this.configuration.accessToken;
            headers = headers.set('Authorization', 'Bearer ' + accessToken);
        }

        // to determine the Accept header
        let httpHeaderAccepts: string[] = [
            'application/json'
        ];
        const httpHeaderAcceptSelected: string | undefined = this.configuration.selectHeaderAccept(httpHeaderAccepts);
        if (httpHeaderAcceptSelected != undefined) {
            headers = headers.set('Accept', httpHeaderAcceptSelected);
        }

        // to determine the Content-Type header
        const consumes: string[] = [
        ];

        return this.httpClient.request<CorrespondenceEventResponse>('post',`${this.basePath}/correspondence/send_correspondence/`,
            {
                params: queryParameters,
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

}
