# Backend endpoints

login = '/api/rest-auth/login/'
dataset = '/api/dataset/'
delete_dataset = '/api/user-dataset/{}/'
dataset_upload = '/api/dataset/{}/upload/'
dataset_folder_content = '/api/user-dataset/{}/contents/{}/'
v1_datasets = '/api/v1/ui/datasets/'
v1_dataset_annotation_sets = '/api/v1/ui/datasets/{}/annotation-sets/'
v1_dataset_image_annotations = '/api/v1/ui/datasets/{}/images/{}/annotations/'
v1_dataset_images = '/api/v1/ui/datasets/{}/images/'
v1_sdk_dataset_images = '/api/v1/sdk/datasets/{}/images/'
v1_sdk_images = '/api/v1/sdk/images/'
v1_annotation_set = '/api/v1/ui/annotation-sets/{}/'
v1_export_annotations = '/api/v1/ui/annotation-sets/{}/export/'
v1_search = '/api/v1/ui/search/'
v1_search_images = '/api/v1/ui/search/?classes={}&tasks={}&dataset_id={}'
v1_search_class = '/api/v1/ui/search/?classes={}'
v1_search_task = '/api/v1/ui/search/?tasks={}'
annotation_set = 'api/annotation-set/{}/'
add_annotation = '/api/dataset/{}/annotation-set/{}/image/{}/save-annotation/'
v1_create_annotation_set = '/api/v1/ui/annotation-sets/'
annotation_info = '/api/dataset/{}/annotation-set/{}/image/{}/annotation/'
