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
 */

export interface InsertContent { 
    contentType: number;
    payload: string;
    sourceId: string;
    sourceType: number;
    userSpecificKey?: string;
}