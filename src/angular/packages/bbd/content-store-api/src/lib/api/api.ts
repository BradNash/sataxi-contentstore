export * from './content.service';
import { ContentService } from './content.service';
export * from './correspondence.service';
import { CorrespondenceService } from './correspondence.service';
export * from './healthCheck.service';
import { HealthCheckService } from './healthCheck.service';
export * from './serverUtils.service';
import { ServerUtilsService } from './serverUtils.service';
export const APIS = [ContentService, CorrespondenceService, HealthCheckService, ServerUtilsService];
