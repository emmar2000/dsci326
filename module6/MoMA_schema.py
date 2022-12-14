from pyspark.sql.types import StructType, StructField, StringType, DateType, IntegerType, DoubleType

exhib_schema = StructType( [StructField('ExhibitionID', IntegerType(), True),
                            StructField('ExhibitionNumber', StringType(), True),
                            StructField('ExhibitionTitle', StringType(), True),
                            StructField('ExhibitionCitationDate', StringType(), True),
                            StructField('ExhibitionBeginDate', DateType(), True),
                            StructField('ExhibitionEndDate', DateType(), True),
                            StructField('ExhibitionSortOrder', StringType(), True),
                            StructField('ExhibitionURL', StringType(), True),
                            StructField('ExhibitionRole', StringType(), True),
                            StructField('ExhibitionRoleinPressRelease', StringType(), True),
                            StructField('ConstituentID', StringType(), True),
                            StructField('ConstituentType', StringType(), True),
                            StructField('DisplayName', StringType(), True),
                            StructField('AlphaSort', StringType(), True),
                            StructField('FirstName', StringType(), True),
                            StructField('MiddleName', StringType(), True),
                            StructField('LastName', StringType(), True),
                            StructField('Suffix', StringType(), True),
                            StructField('Institution', StringType(), True),
                            StructField('Nationality', StringType(), True),
                            StructField('ConstituentBeginDate', IntegerType(), True),
                            StructField('ConstituentEndDate', IntegerType(), True),
                            StructField('ArtistBio', StringType(), True),
                            StructField('Gender', StringType(), True),
                            StructField('VIAFID', StringType(), True),
                            StructField('WikidataID', StringType(), True),
                            StructField('ULANID', StringType(), True),
                            StructField('ConstituentURL', StringType(), True)])
exhib_date_format = "M/d/yyyy"

artwork_schema = StructType([StructField('Title', StringType(), True),
                             StructField('Artist', StringType(), True),
                             StructField('ConstituentID', StringType(), True),
                             StructField('ArtistBio', StringType(), True),
                             StructField('Nationality', StringType(), True),
                             StructField('BeginDate', StringType(), True),
                             StructField('EndDate', StringType(), True),
                             StructField('Gender', StringType(), True),
                             StructField('Date', StringType(), True),
                             StructField('Medium', StringType(), True),
                             StructField('Dimensions', StringType(), True),
                             StructField('CreditLine', StringType(), True),
                             StructField('AccessionNumber', StringType(), True),
                             StructField('Classification', StringType(), True),
                             StructField('Department', StringType(), True),
                             StructField('DateAcquired', StringType(), True),
                             StructField('Cataloged', StringType(), True),
                             StructField('ObjectID', StringType(), True),
                             StructField('URL', StringType(), True),
                             StructField('ThumbnailURL', StringType(), True),
                             StructField('Circumference (cm)', DoubleType(), True),
                             StructField('Depth (cm)', DoubleType(), True),
                             StructField('Diameter (cm)', DoubleType(), True),
                             StructField('Height (cm)', DoubleType(), True),
                             StructField('Length (cm)', DoubleType(), True),
                             StructField('Weight (kg)', DoubleType(), True),
                             StructField('Width (cm)', DoubleType(), True),
                             StructField('Seat Height (cm)', DoubleType(), True),
                             StructField('Duration (sec.)', DoubleType(), True)])