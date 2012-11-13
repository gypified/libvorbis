# This file is used with the GYP meta build system.
# http://code.google.com/p/gyp
# To build try this:
#   svn co http://gyp.googlecode.com/svn/trunk gyp
#   ./gyp/gyp -f make --depth=. libvorbis.gyp
#   make
#   ./out/Debug/test

{
  'variables': {
    'target_arch%': 'ia32', # built for a 32-bit CPU by default
  },
  'target_defaults': {
    'default_configuration': 'Debug',
    'configurations': {
      'Debug': {
        'defines': [ 'DEBUG', '_DEBUG' ],
        'msvs_settings': {
          'VCCLCompilerTool': {
            'RuntimeLibrary': 1, # static debug
          },
        },
      },
      'Release': {
        'defines': [ 'NDEBUG' ],
        'msvs_settings': {
          'VCCLCompilerTool': {
            'RuntimeLibrary': 0, # static release
          },
        },
      }
    },
    'msvs_settings': {
      'VCLinkerTool': {
        'GenerateDebugInformation': 'true',
      },
    },

    # common vorbis stuff
    'defines': [
      'PIC',
      'HAVE_CONFIG_H',
    ],
    'include_dirs': [
      # platform and arch-specific headers
      'config/<(OS)/<(target_arch)',
      'include',
      'lib',
    ],
    'direct_dependent_settings': {
      'include_dirs': [
        # platform and arch-specific headers
        'config/<(OS)/<(target_arch)',
        'include',
      ],
    },
    'conditions': [
      ['OS=="mac"', {
        'defines': [
          'DARWIN',
          'USE_MEMORY_H',
        ],
        'conditions': [
          ['target_arch=="ia32"', { 'xcode_settings': { 'ARCHS': [ 'i386' ] } }],
          ['target_arch=="x64"', { 'xcode_settings': { 'ARCHS': [ 'x86_64' ] } }]
        ],
      }],
    ],
  },

  'targets': [

    # libvorbisenc
    {
      'target_name': 'vorbisenc',
      'product_prefix': 'lib',
      'type': 'static_library',
      'dependencies': [ 'vorbis' ],
      'sources': [
        'lib/vorbisenc.c'
      ]
    },

    # libvorbisfile
    {
      'target_name': 'vorbisfile',
      'product_prefix': 'lib',
      'type': 'static_library',
      'dependencies': [ 'vorbis' ],
      'sources': [
        'lib/vorbisfile.c'
      ]
    },

    # libvorbis
    {
      'target_name': 'vorbis',
      'product_prefix': 'lib',
      'type': 'static_library',
      'sources': [
        'lib/mdct.c',
        'lib/smallft.c',
        'lib/block.c',
        'lib/envelope.c',
        'lib/window.c',
        'lib/lsp.c',
        'lib/lpc.c',
        'lib/analysis.c',
        'lib/synthesis.c',
        'lib/psy.c',
        'lib/info.c',
        'lib/floor1.c',
        'lib/floor0.c',
        'lib/res0.c',
        'lib/mapping0.c',
        'lib/registry.c',
        'lib/codebook.c',
        'lib/sharedbook.c',
        'lib/lookup.c',
        'lib/bitrate.c',
      ],
    },

    {
      'target_name': 'test',
      'type': 'executable',
      'dependencies': [ 'vorbisenc' ],
      'libraries': [
        '-logg' # dependants that use "vorbis" are responsible for making
                # the ogg symbols visible for the resulting executable
      ],
      'sources': [ 't.c' ]
    },
  ]
}
