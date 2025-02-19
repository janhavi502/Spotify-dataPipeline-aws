{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d6c18d2e-0b29-45a3-baa1-56894f5879b5",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Ensure you have AWS credentials configured for S3 uploads.\n",
    "#Set up a config.py file to store API credentials securely:\n",
    "\n",
    "SPOTIFY_CLIENT_ID = \"your_client_id\"\n",
    "SPOTIFY_CLIENT_SECRET = \"your_client_secret\"\n",
    "AWS_S3_BUCKET = \"your_s3_bucket_name\"\n",
    "\n",
    "\n",
    "#Run the ingestion script:\n",
    "python data_ingestion/fetch_spotify_data.py\n",
    "\n",
    "#Run the transformation script:\n",
    "python data_processing/transform_data.py\n",
    "\n",
    "#Load the transformed data into Redshift:\n",
    "psql -h your-redshift-cluster -d database -U user -f database/create_tables.sql"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
