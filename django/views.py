from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class EditorView(View):
    def simple_mode_components(self):
        from resources.models import BoneGroup
        head_bone = BoneGroup.objects.get(name='head')
        neck_bone = BoneGroup.objects.get(name='neck')
        left_arm_bone = BoneGroup.objects.get(name='left arm')
        right_arm_bone = BoneGroup.objects.get(name='right arm')
        left_hand_bone = BoneGroup.objects.get(name='left hand')
        right_hand_bone = BoneGroup.objects.get(name='right hand')
        platform_bone = BoneGroup.objects.get(name='platform')
        handheld_bone = BoneGroup.objects.get(name='weapon')
        body_bone = BoneGroup.objects.get(name='body')
        tail_bone = BoneGroup.objects.get(name='tail')

        return [{
                    'bone': head_bone,
                    'category': "head",
                    'attach_to': '>neck_bone',
                    'attach_point': "#top",
                    'instance_id': '>head_bone'
                },
                {
                    'bone': neck_bone,
                    'category': "neck",
                    'attach_to': '>body_bone',
                    'attach_point': "#neck",
                    'instance_id': '>neck_bone'
                },
                {
                    'bone': body_bone,
                    'category': "body",
                    'attach_to': None,
                    'attach_point': "#palm",
                    'instance_id': '>body_bone'
                },
                {
                    'bone': platform_bone,
                    'category': "platform",
                    'attach_to': '>body_bone',
                    'attach_point': "#platform",
                    'instance_id': '>platform_bone'
                },
                {
                    'bone': left_arm_bone,
                    'category': "left_arm",
                    'attach_to': '>body_bone',
                    'attach_point': "#left arm",
                    'instance_id': '>left_arm_bone'
                },
                {
                    'bone': right_arm_bone,
                    'category': "right_arm",
                    'attach_to': '>body_bone',
                    'attach_point': "#right arm",
                    'instance_id': '>right_arm_bone'
                },
                {
                    'bone': left_hand_bone,
                    'category': "left_hand",
                    'attach_to': '>left_arm_bone',
                    'attach_point': "#hand",
                    'instance_id': '>left_hand_bone'
                },
                {
                    'bone': right_hand_bone,
                    'category': "right_hand",
                    'attach_to': '>right_arm_bone',
                    'attach_point': "#hand",
                    'instance_id': '>right_hand_bone'
                },
                {
                    'bone': handheld_bone,
                    'category': "right_hand_item",
                    'attach_to': '>right_hand_bone',
                    'attach_point': "#palm",
                    'instance_id': '>right_handheld_bone'
                },
                {
                    'bone': handheld_bone,
                    'category': "left_hand_item",
                    'attach_to': '>left_hand_bone',
                    'attach_point': "#palm",
                    'instance_id': '>left_handheld_bone'
                },
                {
                    'bone': tail_bone,
                    'category': 'tail',
                    'attach_to': '>body_bone',
                    'attach_point': "#tail",
                    'instance_id': '>tail_bone'
                }]

    def simple_mode_categories(self):
        from resources.models import Asset, BoneGroup
        head_bone = BoneGroup.objects.get(name='head')
        neck_bone = BoneGroup.objects.get(name='neck')
        left_arm_bone = BoneGroup.objects.get(name='left arm')
        right_arm_bone = BoneGroup.objects.get(name='right arm')
        left_hand_bone = BoneGroup.objects.get(name='left hand')
        right_hand_bone = BoneGroup.objects.get(name='right hand')
        platform_bone = BoneGroup.objects.get(name='platform')
        left_handheld_bone = BoneGroup.objects.get(name='weapon')
        right_handheld_bone = BoneGroup.objects.get(name='weapon')
        body_bone = BoneGroup.objects.get(name='body')

        head_asset = Asset.objects.get(name='male head')
        hair_asset = Asset.objects.get(name='long hair simple')
        neck_asset = Asset.objects.get(name='thick neck')
        shirt_asset = Asset.objects.get(name='simple tunic')
        right_arm_asset = Asset.objects.get(name='muscled arm right')
        left_arm_asset = Asset.objects.get(name='muscled arm left')
        right_hand_asset = Asset.objects.get(name='right hand closed')
        left_hand_asset = Asset.objects.get(name='left hand closed')
        pants_asset = Asset.objects.get(name='male short pants')
        skirts_asset = None
        legwear_asset = None
        footwear_asset = Asset.objects.get(name='male simple shoes')
        platform_asset = Asset.objects.get(name='smooth circular platform')
        weapon_asset = Asset.objects.get(name='shortsword')
        body_asset = Asset.objects.get(name='male body')

        return [{
                    'display_name': 'Head',
                    'name_safe': 'head', # Used to distinguish this group from another group, like left hand and right hand
                    'asset_category': 'head', # corresponds to the data-tab of the tab of assets that should be displayed.
                    'bone_instance_id': '>head_bone',
                    'asset': head_asset
                },
                {
                    'display_name': 'Hair',
                    'name_safe': 'hair',
                    'asset_category': 'hair',
                    'bone_instance_id': '>head_bone',
                    'asset': hair_asset
                },
                {
                    'display_name': 'Headgear',
                    'name_safe': 'headgear',
                    'asset_category': 'headgear',
                    'bone_instance_id': '>head_bone',
                    'asset': None
                },
                # horns
                # ninja mask bottom
                # cape hood & cape hood 2
                # simple mask

                {
                    'display_name': 'Mask',
                    'name_safe': 'mask',
                    'asset_category': 'masks',
                    'bone_instance_id': '>head_bone',
                    'asset': None
                },
                {
                    'display_name': 'Horns',
                    'name_safe': 'horns',
                    'asset_category': 'horns',
                    'bone_instance_id': '>head_bone',
                    'asset': None
                },
                {
                    'display_name': 'Collar',
                    'name_safe': 'collar',
                    'asset_category': 'collars',
                    'bone_instance_id': '>body_bone',
                    'asset': None
                },
                {
                    'display_name': 'Neck',
                    'name_safe': 'neck',
                    'asset_category': 'neck',
                    'bone_instance_id': '>neck_bone',
                    'asset': neck_asset
                },
                {
                    'display_name': 'Body',
                    'name_safe': 'body',
                    'asset_category': 'body',
                    'bone_instance_id': '>body_bone',
                    'asset': body_asset
                },
                {
                    'display_name': 'Shirt (Female)',
                    'name_safe': 'female_shirt',
                    'asset_category': 'female_shirts',
                    'bone_instance_id': '>body_bone',
                    'asset': None
                },
                {
                    'display_name': 'Shirt (Male)',
                    'name_safe': 'male_shirt',
                    'asset_category': 'male_shirts',
                    'bone_instance_id': '>body_bone',
                    'asset': shirt_asset
                },
                {
                    'display_name': 'Left Arm',
                    'name_safe': 'left_arm',
                    'asset_category': 'arms',
                    'bone_instance_id': '>left_arm_bone',
                    'asset': left_arm_asset
                },
                {
                    'display_name': 'Left Hand',
                    'name_safe': 'left_hand',
                    'asset_category': 'hands',
                    'bone_instance_id': '>left_hand_bone',
                    'asset': left_hand_asset
                },
                {
                    'display_name': 'Right Arm',
                    'name_safe': 'right_arm',
                    'asset_category': 'arms',
                    'bone_instance_id': '>right_arm_bone',
                    'asset': right_arm_asset
                },
                {
                    'display_name': 'Right Hand',
                    'name_safe': 'right_hand',
                    'asset_category': 'hands',
                    'bone_instance_id': '>right_hand_bone',
                    'asset': right_hand_asset
                },
                {
                    'display_name': 'Pants',
                    'name_safe': 'pants',
                    'asset_category': 'pants',
                    'bone_instance_id': '>body_bone',
                    'asset': pants_asset
                },
                {
                    'display_name': 'Skirt',
                    'name_safe': 'skirt',
                    'asset_category': 'skirts',
                    'bone_instance_id': '>body_bone',
                    'asset': None
                },
                {
                    'display_name': 'Belt',
                    'name_safe': 'belt',
                    'asset_category': 'belts',
                    'bone_instance_id': '>body_bone',
                    'asset': None
                },
                {
                    'display_name': 'Legwear',
                    'name_safe': 'legwear',
                    'asset_category': 'legwear',
                    'bone_instance_id': '>body_bone',
                    'asset': None
                },
                {
                    'display_name': 'Footwear',
                    'name_safe': 'footwear',
                    'asset_category': 'footwear',
                    'bone_instance_id': '>body_bone',
                    'asset': footwear_asset
                },
                {
                    'display_name': 'Platform',
                    'name_safe': 'platform',
                    'asset_category': 'platforms',
                    'bone_instance_id': '>platform_bone',
                    'asset': platform_asset
                },
                {
                    'display_name': 'Cape',
                    'name_safe': 'cape',
                    'asset_category': 'capes',
                    'bone_instance_id': '>body_bone',
                    'asset': None
                },
                {
                    'display_name': 'Left Hand Item',
                    'name_safe': 'left_hand_item',
                    'asset_category': 'weapons',
                    'bone_instance_id': '>left_handheld_bone',
                    'asset': weapon_asset
                },
                {
                    'display_name': 'Right Hand Item',
                    'name_safe': 'right_hand_item',
                    'asset_category': 'weapons',
                    'bone_instance_id': '>right_handheld_bone',
                    'asset': weapon_asset
                },{
                    'display_name': 'Tail',
                    'name_safe': 'tail',
                    'asset_category': 'tails',
                    'bone_instance_id': '>tail_bone',
                    'asset': None
                },]

    #@method_decorator(login_required)
    def get(self, request):
        from resources.models import Asset, BoneGroup, Pose, Preset
        results = Asset.objects.all().exclude(reviewed=False)
        categories = set([result.category_safe() for result in results])
        bone_groups = BoneGroup.objects.all().exclude(reviewed=False)
        poses = Pose.objects.all().exclude(reviewed=False)
        presets = Preset.objects.all().exclude(reviewed=False)
        return render(request, 'editor_main.html', {'assets': results,
                                                    'categories': categories,
                                                    'bone_groups': bone_groups,
                                                    'poses': poses,
                                                    'presets': presets, 
                                                    'simple_mode_components': self.simple_mode_components(),
                                                    'simple_mode_categories': self.simple_mode_categories()})

from django.contrib.auth import login, authenticate
from resources.forms import RegistrationForm
from django.shortcuts import render, redirect

class RegistrationView(View):
    def get(self, request):
        return render(request, 'registration/register.html', {'form': RegistrationForm()})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.subscribed = form.cleaned_data.get('subscribed')
            user.profile.accepted_terms = form.cleaned_data.get('accepted_terms')
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/editor/')
        return render(request, 'registration/register.html', {'form': form})

class TermsOfServiceView(View):
    def get(self, request):
        return render(request, 'terms_of_service.html')

class PrivacyPolicyView(View):
    def get(self, request):
        return render(request, 'privacy_policy.html')
