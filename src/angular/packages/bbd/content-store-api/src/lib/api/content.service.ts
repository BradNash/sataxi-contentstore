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

import { ContentItem } from '../model/contentItem';
import { FailedResponse } from '../model/failedResponse';
import { InsertContent } from '../model/insertContent';
import { InsertResponseContent } from '../model/insertResponseContent';

import { BASE_PATH, COLLECTION_FORMATS }                     from '../variables';
import { Configuration }                                     from '../configuration';


@Injectable()
export class ContentService {

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
     * Get content
     * @param contentLinkId The content&#x27;s content link id
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public contentContentLinkIdGet(contentLinkId: number, observe?: 'body', reportProgress?: boolean): Observable<ContentItem>;
    public contentContentLinkIdGet(contentLinkId: number, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<ContentItem>>;
    public contentContentLinkIdGet(contentLinkId: number, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<ContentItem>>;
    public contentContentLinkIdGet(contentLinkId: number, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {

        if (contentLinkId === null || contentLinkId === undefined) {
            throw new Error('Required parameter contentLinkId was null or undefined when calling contentContentLinkIdGet.');
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

        return this.httpClient.request<ContentItem>('get',`${this.basePath}/content/${encodeURIComponent(String(contentLinkId))}/`,
            {
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

    /**
     * 
     * Get content by a contentstore uri
     * @param csQueryUri example: cs://123/ OR cs://userSpecifiedKey&#x3D;abc
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public contentFindByCsUriCsQueryUriGet(csQueryUri: string, observe?: 'body', reportProgress?: boolean): Observable<ContentItem>;
    public contentFindByCsUriCsQueryUriGet(csQueryUri: string, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<ContentItem>>;
    public contentFindByCsUriCsQueryUriGet(csQueryUri: string, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<ContentItem>>;
    public contentFindByCsUriCsQueryUriGet(csQueryUri: string, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {

        if (csQueryUri === null || csQueryUri === undefined) {
            throw new Error('Required parameter csQueryUri was null or undefined when calling contentFindByCsUriCsQueryUriGet.');
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

        return this.httpClient.request<ContentItem>('get',`${this.basePath}/content/find_by_cs_uri/${encodeURIComponent(String(csQueryUri))}`,
            {
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

    /**
     * 
     * Upload content
     * @param body Content to be uploaded
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public contentPost(body?: InsertContent, observe?: 'body', reportProgress?: boolean): Observable<InsertResponseContent>;
    public contentPost(body?: InsertContent, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<InsertResponseContent>>;
    public contentPost(body?: InsertContent, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<InsertResponseContent>>;
    public contentPost(body?: InsertContent, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {


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
            'application/json'
        ];
        const httpContentTypeSelected: string | undefined = this.configuration.selectHeaderContentType(consumes);
        if (httpContentTypeSelected != undefined) {
            headers = headers.set('Content-Type', httpContentTypeSelected);
        }

        return this.httpClient.request<InsertResponseContent>('post',`${this.basePath}/content/`,
            {
                body: body,
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

}
