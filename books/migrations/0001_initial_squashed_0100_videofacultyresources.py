# Generated by Django 3.0.4 on 2020-07-16 22:17

import books.models
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import snippets.models
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    replaces = [('books', '0001_initial'), ('books', '0002_auto_20160218_1121'), ('books', '0003_auto_20160222_1200'), ('books', '0004_auto_20160222_1230'), ('books', '0005_auto_20160224_1637'), ('books', '0006_auto_20160225_1410'), ('books', '0007_auto_20160229_1326'), ('books', '0008_book_concept_coach_link'), ('books', '0009_auto_20160307_1106'), ('books', '0010_auto_20160309_1016'), ('books', '0011_book_table_of_contents'), ('books', '0012_book_student_handbook'), ('books', '0013_auto_20160316_1555'), ('books', '0014_book_errata_link'), ('books', '0015_auto_20160328_1056'), ('books', '0016_book_license_text'), ('books', '0017_auto_20160407_1154'), ('books', '0018_book_ibook_link_volume_2'), ('books', '0019_auto_20160419_0955'), ('books', '0020_auto_20160421_2139'), ('books', '0021_auto_20160531_1045'), ('books', '0022_auto_20160617_1216'), ('books', '0023_auto_20160622_1556'), ('books', '0024_book_authors'), ('books', '0025_auto_20160719_1359'), ('books', '0026_auto_20160815_1159'), ('books', '0027_auto_20160901_1548'), ('books', '0028_book_coming_soon'), ('books', '0029_auto_20161025_1300'), ('books', '0030_auto_20161026_1541'), ('books', '0031_auto_20170330_0831'), ('books', '0032_book_comp_copy_available'), ('books', '0033_auto_20170414_0856'), ('books', '0034_book_tutor_marketing_book'), ('books', '0035_auto_20170706_2239'), ('books', '0036_auto_20170707_1305'), ('books', '0037_book_kindle_link'), ('books', '0038_auto_20180125_1347'), ('books', '0039_auto_20180301_1107'), ('books', '0040_auto_20180402_1158'), ('books', '0041_auto_20180403_1123'), ('books', '0042_auto_20180403_1132'), ('books', '0043_auto_20180405_1413'), ('books', '0044_auto_20180405_1452'), ('books', '0045_auto_20180405_1454'), ('books', '0046_auto_20180405_1459'), ('books', '0047_auto_20180405_1531'), ('books', '0048_auto_20180405_1621'), ('books', '0049_auto_20180406_0959'), ('books', '0050_auto_20180406_1002'), ('books', '0051_bookcommunityresources'), ('books', '0052_auto_20180406_1005'), ('books', '0053_auto_20180409_1242'), ('books', '0054_auto_20180418_1034'), ('books', '0055_auto_20180502_1255'), ('books', '0056_auto_20180711_0921'), ('books', '0057_auto_20180713_1227'), ('books', '0058_remove_book_subject'), ('books', '0059_book_subject'), ('books', '0060_auto_20180920_1155'), ('books', '0061_book_chegg_link'), ('books', '0062_book_chegg_link_text'), ('books', '0063_auto_20190220_0836'), ('books', '0064_remove_book_subject'), ('books', '0065_book_book_cover_text_color'), ('books', '0066_auto_20190515_1206'), ('books', '0067_auto_20190710_1351'), ('books', '0068_auto_20190710_1356'), ('books', '0069_auto_20190710_1358'), ('books', '0070_auto_20190710_1424'), ('books', '0071_auto_20190710_1504'), ('books', '0072_book_webview_rex_link'), ('books', '0073_auto_20190730_1437'), ('books', '0073_auto_20190730_1153'), ('books', '0074_merge_20190805_1353'), ('books', '0075_book_study_edge_link'), ('books', '0076_auto_20190805_1642'), ('books', '0077_auto_20190806_1342'), ('books', '0078_auto_20190916_1211'), ('books', '0079_remove_book_table_of_contents'), ('books', '0079_auto_20191003_1236'), ('books', '0080_merge_20191003_1238'), ('books', '0081_book_table_of_contents'), ('books', '0082_book_videos'), ('books', '0083_auto_20191113_1616'), ('books', '0084_auto_20200210_1041'), ('books', '0084_auto_20200203_1638'), ('books', '0085_merge_20200210_1046'), ('books', '0086_auto_20200211_0906'), ('books', '0087_book_partner_page_link_text'), ('books', '0088_auto_20200309_1624'), ('books', '0089_auto_20200309_1627'), ('books', '0090_auto_20200310_1016'), ('books', '0092_auto_20200403_1514'), ('books', '0084_auto_20200213_1156'), ('books', '0087_merge_20200213_1202'), ('books', '0088_merge_20200311_0956'), ('books', '0091_merge_20200325_0813'), ('books', '0093_merge_20200403_1547'), ('books', '0094_auto_20200415_1139'), ('books', '0095_book_use_alt_errata_schedule'), ('books', '0096_auto_20200511_1312'), ('books', '0097_facultyresources_k12'), ('books', '0098_auto_20200710_0830'), ('books', '0099_auto_20200710_0936'), ('books', '0100_videofacultyresources')]

    dependencies = [
        ('wagtaildocs', '0010_document_file_hash'),
        ('wagtailcore', '0040_page_draft_title'),
        ('wagtailcore', '0023_alter_page_revision_on_delete_behaviour'),
        ('snippets', '0002_communityresource'),
        ('snippets', '0001_initial'),
        ('allies', '0001_initial'),
        ('wagtailimages', '0020_add-verbose-name'),
        ('wagtaildocs', '0007_merge'),
        ('snippets', '__first__'),
        ('wagtailimages', '0010_change_on_delete_behaviour'),
        ('snippets', '0010_communityresource_sharedcontent'),
        ('wagtaildocs', '0004_capitalizeverbose'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookAlly',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_link_url', models.URLField(blank=True, help_text='Call to Action Link')),
                ('book_link_text', models.CharField(help_text='Call to Action Text', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='BookIndex',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('page_description', models.TextField()),
                ('dev_standards_heading', models.CharField(blank=True, max_length=255, null=True)),
                ('dev_standard_1_heading', models.CharField(blank=True, max_length=255, null=True)),
                ('dev_standard_1_description', wagtail.fields.RichTextField()),
                ('dev_standard_2_heading', models.CharField(blank=True, max_length=255, null=True)),
                ('dev_standard_2_description', wagtail.fields.RichTextField()),
                ('dev_standard_3_heading', models.CharField(blank=True, max_length=255, null=True)),
                ('dev_standard_3_description', wagtail.fields.RichTextField()),
                ('subject_list_heading', models.CharField(blank=True, max_length=255, null=True)),
                ('promote_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='FacultyResources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_external', models.URLField(blank=True, help_text='Provide an external URL starting with http:// (or fill out either one of the following two).', verbose_name='External link')),
                ('link_document', models.ForeignKey(blank=True, help_text='Or select a document for viewers to download.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.Document')),
                ('link_page', models.ForeignKey(blank=True, help_text='Or select an existing page to attach.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page')),
                ('resource', models.ForeignKey(help_text='Manage resources through snippets.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='snippets.FacultyResource')),
                ('link_text', models.CharField(default='', help_text='Call to Action Text', max_length=255)),
                ('coming_soon_text', models.CharField(blank=True, help_text='If there is text in this field a coming soon banner will be added with this description.', max_length=255, null=True)),
                ('updated', models.DateTimeField(blank=True, help_text='Late date resource was updated', null=True)),
                ('featured', models.BooleanField(default=False, help_text='Add to featured bar on resource page')),
                ('k12', models.BooleanField(default=False, help_text='Add K12 banner to resource')),
                ('video_reference_number', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote_text', wagtail.fields.RichTextField()),
                ('quote_author', models.CharField(max_length=255)),
                ('quote_author_school', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('cnx_id', models.CharField(blank=True, help_text='This is used to pull relevant information from CNX.', max_length=255, null=True)),
                ('updated', models.DateTimeField(blank=True, help_text='Late date web content was updated', null=True)),
                ('description', wagtail.fields.RichTextField(blank=True, help_text='Description shown on Book Detail page.')),
                ('publish_date', models.DateField(help_text='Date the book is published on.', null=True)),
                ('print_isbn_10', models.CharField(blank=True, help_text='ISBN 10 for print version (hardcover).', max_length=255, null=True)),
                ('print_isbn_13', models.CharField(blank=True, help_text='ISBN 13 for print version (hardcover).', max_length=255, null=True)),
                ('license_name', models.CharField(blank=True, editable=False, help_text='Name of the license.', max_length=255, null=True)),
                ('license_version', models.CharField(blank=True, editable=False, help_text='Version of the license.', max_length=255, null=True)),
                ('license_url', models.CharField(blank=True, editable=False, help_text='External URL of the license.', max_length=255, null=True)),
                ('cover', models.ForeignKey(help_text='The book cover to be shown on the website.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.Document')),
                ('is_ap', models.BooleanField(default=False, help_text='Whether this book is an AP (Advanced Placement) book.')),
                ('high_resolution_pdf', models.ForeignKey(blank=True, help_text='High quality PDF document of the book.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.Document')),
                ('ibook_link', models.URLField(blank=True, help_text='Link to iBook')),
                ('low_resolution_pdf', models.ForeignKey(blank=True, help_text='Low quality PDF document of the book.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.Document')),
                ('webview_link', models.URLField(blank=True, help_text='Link to CNX Webview book')),
                ('amazon_link', models.URLField(blank=True, help_text='Link to Amazon')),
                ('bookshare_link', models.URLField(blank=True, help_text='Link to Bookshare resources')),
                ('license_text', models.TextField(blank=True, help_text='Overrides default license text.', null=True)),
                ('ibook_link_volume_2', models.URLField(blank=True, help_text='Link to secondary iBook')),
                ('community_resource_cta', models.CharField(blank=True, help_text='Call the action text.', max_length=255, null=True)),
                ('community_resource_url', models.URLField(blank=True, help_text='URL of the external source.')),
                ('authors', wagtail.fields.StreamField([('author', wagtail.blocks.StructBlock([('name', wagtail.blocks.CharBlock(help_text='Full name of the author.', required=True)), ('university', wagtail.blocks.CharBlock(help_text='Name of the university/institution the author is associated with.', required=False)), ('country', wagtail.blocks.CharBlock(help_text='Country of the university/institution.', required=False)), ('senior_author', wagtail.blocks.BooleanBlock(help_text='Whether the author is a senior author. (Senior authors are shown before non-senior authors.)', required=False)), ('display_at_top', wagtail.blocks.BooleanBlock(help_text='Whether display the author on top.', required=False))]))], null=True)),
                ('coming_soon', models.BooleanField(default=False)),
                ('salesforce_abbreviation', models.CharField(blank=True, max_length=255, null=True)),
                ('salesforce_name', models.CharField(blank=True, max_length=255, null=True)),
                ('amazon_coming_soon', models.BooleanField(default=False, help_text='Whether this book is coming to Amazon bookstore.')),
                ('bookstore_coming_soon', models.BooleanField(default=False, help_text='Whether this book is coming to bookstore soon.')),
                ('comp_copy_available', models.BooleanField(default=True, help_text='Whether free compy available for teachers.')),
                ('tutor_marketing_book', models.BooleanField(default=False, help_text='Whether this is a Tutor marketing book.')),
                ('digital_isbn_10', models.CharField(blank=True, help_text='ISBN 10 for digital version.', max_length=255, null=True)),
                ('digital_isbn_13', models.CharField(blank=True, help_text='ISBN 13 for digital version.', max_length=255, null=True)),
                ('ibook_isbn_10', models.CharField(blank=True, help_text='ISBN 10 for iBook version.', max_length=255, null=True)),
                ('ibook_isbn_13', models.CharField(blank=True, help_text='ISBN 13 for iBook version.', max_length=255, null=True)),
                ('ibook_volume_2_isbn_10', models.CharField(blank=True, help_text='ISBN 10 for iBook v2 version.', max_length=255, null=True)),
                ('ibook_volume_2_isbn_13', models.CharField(blank=True, help_text='ISBN 13 for iBook v2 version.', max_length=255, null=True)),
                ('kindle_link', models.URLField(blank=True, help_text='Link to Kindle version')),
                ('community_resource_blurb', models.TextField(blank=True, help_text='Blurb.')),
                ('community_resource_feature_text', models.TextField(blank=True, help_text='Text of the community resource feature.')),
                ('cover_color', models.CharField(choices=[('blue', 'Blue'), ('deep-green', 'Deep Green'), ('gold', 'Gold'), ('gray', 'Gray'), ('green', 'Green'), ('light-blue', 'Light Blue'), ('light-gray', 'Light Gray'), ('medium-blue', 'Medium Blue'), ('orange', 'Orange'), ('red', 'Red'), ('yellow', 'Yellow')], default='blue', help_text='The color of the cover.', max_length=255)),
                ('reverse_gradient', models.BooleanField(default=False)),
                ('title_image', models.ForeignKey(help_text='The svg for title image to be shown on the website.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.Document')),
                ('community_resource_feature_link', models.ForeignKey(blank=True, help_text='Document of the community resource feature.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.Document')),
                ('ally_content', wagtail.fields.StreamField([('content', books.models.SharedContentChooserBlock(snippets.models.SharedContent)), ('link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.CharBlock(required=False))], blank=True, null=True)),
                ('bookstore_content', wagtail.fields.StreamField([('content', books.models.SharedContentChooserBlock(snippets.models.SharedContent)), ('link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.CharBlock(required=False))], blank=True, help_text='Bookstore content.', null=True)),
                ('comp_copy_content', wagtail.fields.StreamField([('content', books.models.SharedContentChooserBlock(snippets.models.SharedContent)), ('link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.CharBlock(required=False))], blank=True, help_text='Content of the free copy.', null=True)),
                ('errata_content', wagtail.fields.StreamField([('content', books.models.SharedContentChooserBlock(snippets.models.SharedContent)), ('link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.CharBlock(required=False))], blank=True, help_text='Errata content.', null=True)),
                ('free_stuff_instructor', wagtail.fields.StreamField([('content', books.models.SharedContentChooserBlock(snippets.models.SharedContent)), ('link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.CharBlock(required=False))], blank=True, help_text='Snippet to show texts for free instructor resources.', null=True)),
                ('free_stuff_student', wagtail.fields.StreamField([('content', books.models.SharedContentChooserBlock(snippets.models.SharedContent)), ('link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.CharBlock(required=False))], blank=True, help_text='Snipped to show texts for free student resources.', null=True)),
                ('webinar_content', wagtail.fields.StreamField([('content', books.models.SharedContentChooserBlock(snippets.models.SharedContent)), ('link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.CharBlock(required=False))], blank=True, null=True)),
                ('community_resource_heading', models.CharField(blank=True, help_text='Snipped to show texts for community resources.', max_length=255, null=True)),
                ('community_resource_logo', models.ForeignKey(blank=True, help_text='Logo for community resources.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.Document')),
                ('book_state', models.CharField(choices=[('live', 'Live'), ('coming_soon', 'Coming Soon'), ('new_edition_available', 'New Edition Available (Show new edition correction schedule)'), ('deprecated', 'Deprecated (Disallow errata submissions and show deprecated schedule)'), ('retired', 'Retired (Remove from website)')], default='live', help_text='The state of the book.', max_length=255)),
                ('promote_image', models.ForeignKey(blank=True, help_text='Promote image.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('chegg_link', models.URLField(blank=True, help_text='Link to Chegg e-reader', null=True)),
                ('chegg_link_text', models.CharField(blank=True, help_text='Text for Chegg link.', max_length=255, null=True)),
                ('book_cover_text_color', models.CharField(choices=[('yellow', 'Yellow'), ('light_blue', 'Light Blue'), ('dark_blue', 'Dark Blue'), ('green', 'Green'), ('white', 'White'), ('grey', 'Grey'), ('red', 'Red'), ('white_red', 'White/Red'), ('white_blue', 'White/Blue'), ('green_white', 'Green/White'), ('yellow_white', 'Yellow/White'), ('grey_white', 'Grey/White'), ('white_grey', 'White/Grey'), ('white_orange', 'White/Orange')], default='yellow', help_text='Use by the Unified team - this will not change the text color on the book cover.', max_length=255)),
                ('webview_rex_link', models.URLField(blank=True, help_text='Link to REX Webview book')),
                ('print_softcover_isbn_10', models.CharField(blank=True, help_text='ISBN 10 for print version (softcover).', max_length=255, null=True)),
                ('print_softcover_isbn_13', models.CharField(blank=True, help_text='ISBN 13 for print version (softcover).', max_length=255, null=True)),
                ('last_updated_pdf', models.DateTimeField(blank=True, help_text='Last time PDF was revised.', null=True, verbose_name='PDF Content Revision Date')),
                ('enable_study_edge', models.BooleanField(default=False, help_text='This will cause the link to the Study Edge app appear on the book details page.')),
                ('rex_callout_blurb', models.CharField(blank=True, help_text='Additional text for the REX callout.', max_length=255, null=True)),
                ('rex_callout_title', models.CharField(blank=True, default='Recommended', help_text='Title of the REX callout', max_length=255, null=True)),
                ('table_of_contents', django.contrib.postgres.fields.jsonb.JSONField(blank=True, editable=False, help_text='TOC.', null=True)),
                ('videos', wagtail.fields.StreamField([('video', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('description', wagtail.blocks.RichTextBlock()), ('embed', wagtail.blocks.RawHTMLBlock())])))], blank=True, null=True)),
                ('partner_list_label', models.CharField(blank=True, help_text='Controls the heading text on the book detail page for partners. This will update ALL books to use this value!', max_length=255, null=True)),
                ('partner_page_link_text', models.CharField(blank=True, help_text='Link to partners page on top right of list.', max_length=255, null=True)),
                ('featured_resources_header', models.CharField(blank=True, help_text='Featured resource header on instructor resources tab.', max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Full name of the author.', max_length=255)),
                ('university', models.CharField(blank=True, help_text='Name of the university/institution the author is associated with.', max_length=255, null=True)),
                ('country', models.CharField(blank=True, help_text='Country of the university/institution.', max_length=255, null=True)),
                ('senior_author', models.BooleanField(default=False, help_text='Whether the author is a senior author. (Senior authors are shown before non-senior authors.)')),
                ('display_at_top', models.BooleanField(default=False, help_text='Whether display the author on top.')),
                ('book', modelcluster.fields.ParentalKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='book_contributing_authors', to='books.Book')),
            ],
        ),
        migrations.CreateModel(
            name='BookQuotes',
            fields=[
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=('books.quotes', models.Model),
        ),
        migrations.CreateModel(
            name='BookFacultyResources',
            fields=[
                ('facultyresources_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='books.FacultyResources')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('book_faculty_resource', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_faculty_resources', to='books.Book')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=('books.facultyresources', models.Model),
        ),
        migrations.CreateModel(
            name='BookAllies',
            fields=[
                ('bookally_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='books.BookAlly')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('book_ally', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_allies', to='books.Book')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=('books.bookally', models.Model),
        ),
        migrations.CreateModel(
            name='StudentResources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_external', models.URLField(blank=True, help_text='Provide an external URL starting with http:// (or fill out either one of the following two).', verbose_name='External link')),
                ('link_text', models.CharField(help_text='Call to Action Text', max_length=255)),
                ('link_document', models.ForeignKey(blank=True, help_text='Or select a document for viewers to download.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.Document')),
                ('link_page', models.ForeignKey(blank=True, help_text='Or select an existing page to attach.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page')),
                ('resource', models.ForeignKey(help_text='Manage resources through snippets.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='snippets.StudentResource')),
                ('coming_soon_text', models.CharField(blank=True, help_text='If there is text in this field a coming soon banner will be added with this description.', max_length=255, null=True)),
                ('updated', models.DateTimeField(blank=True, help_text='Late date resource was updated', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BookStudentResources',
            fields=[
                ('studentresources_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='books.StudentResources')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('book_student_resource', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_student_resources', to='books.Book')),
            ],
            options={
                'abstract': False,
                'ordering': ['sort_order'],
            },
            bases=('books.studentresources', models.Model),
        ),
        migrations.CreateModel(
            name='BookSharedContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(blank=True, null=True)),
                ('link_text', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BookSharedContents',
            fields=[
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
            ],
            options={
                'abstract': False,
                'ordering': ['sort_order'],
            },
            bases=('books.booksharedcontent', models.Model),
        ),
        migrations.DeleteModel(
            name='BookSharedContent',
        ),
        migrations.DeleteModel(
            name='BookSharedContents',
        ),
        migrations.DeleteModel(
            name='BookQuotes',
        ),
        migrations.DeleteModel(
            name='Quotes',
        ),
        migrations.CreateModel(
            name='SubjectBooks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subjects_subject', to='snippets.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='BookSubjects',
            fields=[
                ('subjectbooks_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='books.SubjectBooks')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('book_subject', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_subjects', to='books.Book')),
            ],
            options={
                'abstract': False,
                'ordering': ['sort_order'],
            },
            bases=('books.subjectbooks', models.Model),
        ),
        migrations.DeleteModel(
            name='BookAllies',
        ),
        migrations.DeleteModel(
            name='BookAlly',
        ),
        migrations.CreateModel(
            name='VideoFacultyResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource_heading', models.CharField(max_length=255)),
                ('resource_description', wagtail.fields.RichTextField(blank=True, null=True)),
                ('video_title', models.CharField(blank=True, max_length=255, null=True)),
                ('video_url', models.URLField(blank=True, null=True)),
                ('video_file', models.FileField(blank=True, null=True, upload_to='resource_videos')),
            ],
        ),
        migrations.CreateModel(
            name='VideoFacultyResources',
            fields=[
                ('videofacultyresource_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='books.VideoFacultyResource')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('book_video_faculty_resource', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_video_faculty_resources', to='books.Book')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=('books.videofacultyresource', models.Model),
        ),
    ]
