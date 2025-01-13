import datasets
pip install datasets
c
clear
import datasets
datasets.logging.set_verbosity_error()
from datasets import load_dataset
dataset = load_dataset("McAuley-Lab/Amazon-Reviews-2023", "raw_review_All_Beauty", trust_remote_code=True)
dataset["full"][0]
{'rating': 5.0,
 'title': 'Such a lovely scent but not overpowering.',
 'text': "This spray is really nice. It smells really good, goes on really fine, and does the trick. I will say it feels like you need a lot of it though to get the texture I want. I have a lot of hair, medium thickness. I am comparing to other brands with yucky chemicals so I'm gonna stick with this. Try it!",
 'images': [],
 'asin': 'B00YQ6X8EO',
 'parent_asin': 'B00YQ6X8EO',
 'user_id': 'AGKHLEW2SOWHNMFQIJGBECAF7INQ',
 'timestamp': 1588687728923,
 'helpful_vote': 0,
 'verified_purchase': True}
len(dataset)
1
dataset.shape
{'full': (701528, 10)}
dataset["full"][1]
{'rating': 4.0,
 'title': 'Works great but smells a little weird.',
 'text': 'This product does what I need it to do, I just wish it was odorless or had a soft coconut smell. Having my head smell like an orange coffee is offputting. (granted, I did know the smell was described but I was hoping it would be light)',
 'images': [],
 'asin': 'B081TJ8YS3',
 'parent_asin': 'B081TJ8YS3',
 'user_id': 'AGKHLEW2SOWHNMFQIJGBECAF7INQ',
 'timestamp': 1588615855070,
 'helpful_vote': 1,
 'verified_purchase': True}
c
clear
dataset_item = load_dataset("McAuley-Lab/Amazon-Reviews-2023", "raw_meta_All_Beauty", split="full", trust_remote_code=True)
dataset_item[0]
{'main_category': 'All Beauty',
 'title': 'Howard LC0008 Leather Conditioner, 8-Ounce (4-Pack)',
 'average_rating': 4.8,
 'rating_number': 10,
 'features': [],
 'description': [],
 'price': 'None',
 'images': {'hi_res': [None,
   'https://m.media-amazon.com/images/I/71i77AuI9xL._SL1500_.jpg'],
  'large': ['https://m.media-amazon.com/images/I/41qfjSfqNyL.jpg',
   'https://m.media-amazon.com/images/I/41w2yznfuZL.jpg'],
  'thumb': ['https://m.media-amazon.com/images/I/41qfjSfqNyL._SS40_.jpg',
   'https://m.media-amazon.com/images/I/41w2yznfuZL._SS40_.jpg'],
  'variant': ['MAIN', 'PT01']},
 'videos': {'title': [], 'url': [], 'user_id': []},
 'store': 'Howard Products',
 'categories': [],
 'details': '{"Package Dimensions": "7.1 x 5.5 x 3 inches; 2.38 Pounds", "UPC": "617390882781"}',
 'parent_asin': 'B01CUPMQZE',
 'bought_together': None,
 'subtitle': None,
 'author': None}
clear
type(dataset)
datasets.dataset_dict.DatasetDict
dataset["full"][1]
{'rating': 4.0,
 'title': 'Works great but smells a little weird.',
 'text': 'This product does what I need it to do, I just wish it was odorless or had a soft coconut smell. Having my head smell like an orange coffee is offputting. (granted, I did know the smell was described but I was hoping it would be light)',
 'images': [],
 'asin': 'B081TJ8YS3',
 'parent_asin': 'B081TJ8YS3',
 'user_id': 'AGKHLEW2SOWHNMFQIJGBECAF7INQ',
 'timestamp': 1588615855070,
 'helpful_vote': 1,
 'verified_purchase': True}
dataset.shape
{'full': (701528, 10)}
dataset_item[0]
{'main_category': 'All Beauty',
 'title': 'Howard LC0008 Leather Conditioner, 8-Ounce (4-Pack)',
 'average_rating': 4.8,
 'rating_number': 10,
 'features': [],
 'description': [],
 'price': 'None',
 'images': {'hi_res': [None,
   'https://m.media-amazon.com/images/I/71i77AuI9xL._SL1500_.jpg'],
  'large': ['https://m.media-amazon.com/images/I/41qfjSfqNyL.jpg',
   'https://m.media-amazon.com/images/I/41w2yznfuZL.jpg'],
  'thumb': ['https://m.media-amazon.com/images/I/41qfjSfqNyL._SS40_.jpg',
   'https://m.media-amazon.com/images/I/41w2yznfuZL._SS40_.jpg'],
  'variant': ['MAIN', 'PT01']},
 'videos': {'title': [], 'url': [], 'user_id': []},
 'store': 'Howard Products',
 'categories': [],
 'details': '{"Package Dimensions": "7.1 x 5.5 x 3 inches; 2.38 Pounds", "UPC": "617390882781"}',
 'parent_asin': 'B01CUPMQZE',
 'bought_together': None,
 'subtitle': None,
 'author': None}
clear
import pandas as pd
product_df = pd.DataFrame(dataset)
clear
product_df = pd.DataFrame(dataset_item)
review_df = pd.DataFrame(dataset)
selected_products = products_df[['parent_asin', 'title']].head(10)
selected_products = product_df[['parent_asin', 'title']].head(10)
filtered_reviews = review_df[review_df['parent_asin'].isin(selected_products['parent_asin'])]
filtered_reviews = review_df[review_df['parent_asin'].isin(product_df['parent_asin'])]
clear
filtered_reviews = review_df[review_df['parent_asin'].isin(product_df['parent_asin'])]
clear
review_df.head()
                                                full
0  {'rating': 5.0, 'title': 'Such a lovely scent ...
1  {'rating': 4.0, 'title': 'Works great but smel...
2  {'rating': 5.0, 'title': 'Yes!', 'text': 'Smel...
3  {'rating': 1.0, 'title': 'Synthetic feeling', ...
4  {'rating': 5.0, 'title': 'A+', 'text': 'Love i...
product_df.head()
  main_category                                              title  average_rating  rating_number  ... parent_asin bought_together subtitle author
0    All Beauty  Howard LC0008 Leather Conditioner, 8-Ounce (4-...             4.8             10  ...  B01CUPMQZE            None     None   None
1    All Beauty  Yes to Tomatoes Detoxifying Charcoal Cleanser ...             4.5              3  ...  B076WQZGPM            None     None   None
2    All Beauty   Eye Patch Black Adult with Tie Band (6 Per Pack)             4.4             26  ...  B000B658RI            None     None   None
3    All Beauty  Tattoo Eyebrow Stickers, Waterproof Eyebrow, 4...             3.1            102  ...  B088FKY3VD            None     None   None
4    All Beauty  Precision Plunger Bars for Cartridge Grips – 9...             4.3              7  ...  B07NGFDN6G            None     None   None

[5 rows x 16 columns]
filtered_reviews = review_df[review_df['parent_asin'].isin(product_df['parent_asin'])]
print(review_df.columns)
print(product_df.columns)
review_df = pd.DataFrame(dataset["full"])
filtered_reviews = review_df[review_df['parent_asin'].isin(product_df['parent_asin'])]
filtered_reviews
        rating                                      title                                               text  ...      timestamp helpful_vote verified_purchase
0          5.0  Such a lovely scent but not overpowering.  This spray is really nice. It smells really go...  ...  1588687728923            0              True
1          4.0     Works great but smells a little weird.  This product does what I need it to do, I just...  ...  1588615855070            1              True
2          5.0                                       Yes!                          Smells good, feels great!  ...  1589665266052            2              True
3          1.0                          Synthetic feeling                                     Felt synthetic  ...  1643393630220            0              True
4          5.0                                         A+                                            Love it  ...  1609322563534            0              True
...        ...                                        ...                                                ...  ...            ...          ...               ...
701523     4.0                                 Four Stars    Conditioner is great  shampoo not as I expected  ...  1478227021000            0              True
701524     1.0                                     Pretty  Did not work! Used the whole bottle and my hai...  ...  1480908730000            0             False
701525     5.0                       Great sunless tanner         Product as expected. Shipping was on time.  ...  1590547974067            0              True
701526     5.0              The Crown on top is a Ring!!!  Not only is it a delicious fragrance, but also...  ...  1184798209000            4             False
701527     4.0                   Good Shampoo/Conditioner  The conditioner doesn't really make your hair ...  ...  1366944486000            1              True

[701528 rows x 10 columns]
limited_reviews = filtered_reviews.groupby('parent_asin').head(10)
limited_reviews
        rating                                              title  ... helpful_vote verified_purchase
0          5.0          Such a lovely scent but not overpowering.  ...            0              True
1          4.0             Works great but smells a little weird.  ...            1              True
2          5.0                                               Yes!  ...            2              True
3          1.0                                  Synthetic feeling  ...            0              True
4          5.0                                                 A+  ...            0              True
...        ...                                                ...  ...          ...               ...
701516     1.0                                Not a good product.  ...            0              True
701517     1.0  I hate it, the hair is very thin!!!!! I was ve...  ...            0              True
701518     1.0                                           One Star  ...            0              True
701519     1.0                                           One Star  ...            0              True
701525     5.0                               Great sunless tanner  ...            0              True

[371836 rows x 10 columns]
limited_reviews.columns
Index(['rating', 'title', 'text', 'images', 'asin', 'parent_asin', 'user_id',
       'timestamp', 'helpful_vote', 'verified_purchase'],
      dtype='object')
selected_products
  parent_asin                                              title
0  B01CUPMQZE  Howard LC0008 Leather Conditioner, 8-Ounce (4-...
1  B076WQZGPM  Yes to Tomatoes Detoxifying Charcoal Cleanser ...
2  B000B658RI   Eye Patch Black Adult with Tie Band (6 Per Pack)
3  B088FKY3VD  Tattoo Eyebrow Stickers, Waterproof Eyebrow, 4...
4  B07NGFDN6G  Precision Plunger Bars for Cartridge Grips – 9...
5  B07G9GWFSM  Lurrose 100Pcs Full Cover Fake Toenails Artifi...
6  B08XZ97HFY  Stain Bonnet For Baby Bonnet Silk Sleep Cap Fo...
7  B08DNQTTQK  50 Pieces False Eyelash Packaging Box Empty Ey...
8  B01ERJEGS6                         Gold extatic Musk EDT 90ml
9  B08P7LXKP7  4 Pieces Satin Bonnet Adjustable Sleep Cap Dou...
selected_products.shape
(10, 2)
limited_reviews['parent_asin'].unique()
array(['B00YQ6X8EO', 'B081TJ8YS3', 'B097R46CSY', ..., 'B0BW8D688K',
       'B07F9D8RMB', 'B098QZBNMD'], dtype=object)
len(limited_reviews['parent_asin'].unique())
112565
review_df.shape
(701528, 10)
merged_df = pd.merge(review_df, selected_products, on='parent_asin', how='inner')
merged_df.shape
(47, 11)
merged_df.unique
merged_df.columns
Index(['rating', 'title_x', 'text', 'images', 'asin', 'parent_asin', 'user_id',
       'timestamp', 'helpful_vote', 'verified_purchase', 'title_y'],
      dtype='object')
merged_df
    rating                                            title_x  ... verified_purchase                                            title_y
0      5.0                                         Five Stars  ...              True   Eye Patch Black Adult with Tie Band (6 Per Pack)
1      5.0                                               Nice  ...              True   Eye Patch Black Adult with Tie Band (6 Per Pack)
2      2.0             Flimsy storage container breaks easily  ...             False  Lurrose 100Pcs Full Cover Fake Toenails Artifi...
3      5.0  Absolutely fabulous - I will never use anythin...  ...              True  Howard LC0008 Leather Conditioner, 8-Ounce (4-...
4      3.0             Useful for temporary use or dirty work  ...              True   Eye Patch Black Adult with Tie Band (6 Per Pack)
5      5.0                                           Nice fit  ...              True  Stain Bonnet For Baby Bonnet Silk Sleep Cap Fo...
6      3.0                                        Three Stars  ...              True   Eye Patch Black Adult with Tie Band (6 Per Pack)
7      5.0  Missing Review.......... It’s lost at Amazon S...  ...              True  Precision Plunger Bars for Cartridge Grips – 9...
8      5.0                                       Satin bonnet  ...              True  4 Pieces Satin Bonnet Adjustable Sleep Cap Dou...
9      1.0                         Not at all what I excepted  ...             False  Tattoo Eyebrow Stickers, Waterproof Eyebrow, 4...
10     5.0                                        works great  ...              True   Eye Patch Black Adult with Tie Band (6 Per Pack)
11     5.0                                       Nice perfume  ...              True                         Gold extatic Musk EDT 90ml
12     5.0                                         Five Stars  ...              True  Yes to Tomatoes Detoxifying Charcoal Cleanser ...
13     2.0  When you get it right. Takes practice. It stay...  ...              True  Tattoo Eyebrow Stickers, Waterproof Eyebrow, 4...
14     1.0                                               Size  ...              True  Stain Bonnet For Baby Bonnet Silk Sleep Cap Fo...
15     2.0                               Don't buy for babies  ...              True  Stain Bonnet For Baby Bonnet Silk Sleep Cap Fo...
16     3.0                                       Nice but big  ...              True  4 Pieces Satin Bonnet Adjustable Sleep Cap Dou...
17     5.0                                   Natural looking.  ...              True  Tattoo Eyebrow Stickers, Waterproof Eyebrow, 4...
18     5.0  Of all leather products I have used this one s...  ...              True  Howard LC0008 Leather Conditioner, 8-Ounce (4-...
19     2.0  Gold Exotic by Balmain may be a great fragranc...  ...              True                         Gold extatic Musk EDT 90ml
20     4.0                                     Just a tad big  ...              True  4 Pieces Satin Bonnet Adjustable Sleep Cap Dou...
21     5.0                            Great for your business  ...              True  50 Pieces False Eyelash Packaging Box Empty Ey...
22     4.0                                      Looks Natural  ...              True  Tattoo Eyebrow Stickers, Waterproof Eyebrow, 4...
23     3.0                                        eye patches  ...              True   Eye Patch Black Adult with Tie Band (6 Per Pack)
24     5.0                                         Five Stars  ...              True   Eye Patch Black Adult with Tie Band (6 Per Pack)
25     1.0                                         There junk  ...              True  Tattoo Eyebrow Stickers, Waterproof Eyebrow, 4...
26     1.0                 Don’t waste money on this product.  ...              True  Tattoo Eyebrow Stickers, Waterproof Eyebrow, 4...
27     5.0                                Amazingly Realistic  ...              True  Tattoo Eyebrow Stickers, Waterproof Eyebrow, 4...
28     3.0  As some people have described, these are large...  ...              True   Eye Patch Black Adult with Tie Band (6 Per Pack)
29     5.0                                         Five Stars  ...              True   Eye Patch Black Adult with Tie Band (6 Per Pack)
30     5.0                            soft, comfy, adjustable  ...              True  4 Pieces Satin Bonnet Adjustable Sleep Cap Dou...
31     5.0                                              Cute!  ...             False  Stain Bonnet For Baby Bonnet Silk Sleep Cap Fo...
32     1.0                     We laughed and we laughed hard  ...              True  Tattoo Eyebrow Stickers, Waterproof Eyebrow, 4...
33     5.0                                       Eyebrows yay  ...              True  Tattoo Eyebrow Stickers, Waterproof Eyebrow, 4...
34     5.0                                  Oh Happy Mistake!  ...              True   Eye Patch Black Adult with Tie Band (6 Per Pack)
35     5.0                                         Five Stars  ...              True   Eye Patch Black Adult with Tie Band (6 Per Pack)
36     4.0                       Product works as advertised.  ...              True  Howard LC0008 Leather Conditioner, 8-Ounce (4-...
37     5.0                                        Great stuff  ...              True  Howard LC0008 Leather Conditioner, 8-Ounce (4-...
38     4.0                      Keeps leather from drying out  ...              True  Howard LC0008 Leather Conditioner, 8-Ounce (4-...
39     4.0                                         Four Stars  ...              True   Eye Patch Black Adult with Tie Band (6 Per Pack)
40     5.0                                     Good Eye Patch  ...              True   Eye Patch Black Adult with Tie Band (6 Per Pack)
41     2.0         Best for people with shaved or no eyebrows  ...              True  Tattoo Eyebrow Stickers, Waterproof Eyebrow, 4...
42     5.0                      Wonderful and super realistic  ...              True  Tattoo Eyebrow Stickers, Waterproof Eyebrow, 4...
43     5.0                      Great quality worth the money  ...              True  50 Pieces False Eyelash Packaging Box Empty Ey...
44     5.0                                everything was fine  ...              True   Eye Patch Black Adult with Tie Band (6 Per Pack)
45     3.0                                      Cracked cases  ...              True  50 Pieces False Eyelash Packaging Box Empty Ey...
46     5.0                                             Babies  ...              True  Stain Bonnet For Baby Bonnet Silk Sleep Cap Fo...

[47 rows x 11 columns]
json_file_path = './merged_reviews.json'
merged_df.to_json(json_file_path, orient='records', lines=True)
ls
review_df.columns
Index(['rating', 'title', 'text', 'images', 'asin', 'parent_asin', 'user_id',
       'timestamp', 'helpful_vote', 'verified_purchase'],
      dtype='object')
review_df[0]
review_df.head(1)
   rating                                      title                                               text  ...      timestamp helpful_vote verified_purchase
0     5.0  Such a lovely scent but not overpowering.  This spray is really nice. It smells really go...  ...  1588687728923            0              True

[1 rows x 10 columns]
review_df.columns
Index(['rating', 'title', 'text', 'images', 'asin', 'parent_asin', 'user_id',
       'timestamp', 'helpful_vote', 'verified_purchase'],
      dtype='object')
clear
product_df.head(1)
  main_category                                              title  average_rating  rating_number  ... parent_asin bought_together subtitle author
0    All Beauty  Howard LC0008 Leather Conditioner, 8-Ounce (4-...             4.8             10  ...  B01CUPMQZE            None     None   None

[1 rows x 16 columns]
product_df.coloumns
product_df.columns
Index(['main_category', 'title', 'average_rating', 'rating_number', 'features',
       'description', 'price', 'images', 'videos', 'store', 'categories',
       'details', 'parent_asin', 'bought_together', 'subtitle', 'author'],
      dtype='object')
product_df['subtitle'].head(1)
0    None
Name: subtitle, dtype: object
product_df['title'].head(1)
0    Howard LC0008 Leather Conditioner, 8-Ounce (4-...
Name: title, dtype: object
product_df['main_category'].head(1)
0    All Beauty
Name: main_category, dtype: object
%history -f previous.py -o
