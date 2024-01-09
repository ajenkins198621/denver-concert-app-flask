#!/usr/bin/env python3

from flask import Flask, request

app = Flask(__name__)


def get_header(title: str) -> str:
    """ gets the header content """
    return f'''
        <html>
        <head>
            <title>{title}</title>
        </head>
        <body style="margin: 0; padding: 0; background-color: #dedede;">
        <nav style="display: flex; padding: 16px; background-color: #080808; color: white; font-size: 24px; justify-content: center;">
            <a href="/">
                <svg width="300" height="100" viewBox="0 0 205 50" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <g clip-path="url(#clip0_0_1)">
                    <path d="M12 41.8333H48.75L34.6196 12.0005C34.2392 11.1966 33.6383 10.5172 32.8869 10.0415C32.1355 9.56571 31.2644 9.31314 30.375 9.31314C29.4856 9.31314 28.6145 9.56571 27.8631 10.0415C27.1117 10.5172 26.5108 11.1966 26.1304 12.0005L12 41.8333Z" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M21.1875 23.4583L25.2708 28.5625L30.375 23.4583L34.4583 29.5833L39.5625 25.5" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    </g>
                    <path d="M202.315 33.1139L203.874 12.0887C203.959 11.1049 203.653 10.1272 203.024 9.36619C202.395 8.60519 201.492 8.12177 200.51 8.02005C199.528 7.91833 198.545 8.20644 197.773 8.82234C197.001 9.43823 196.502 10.3326 196.383 11.3129L195.149 20.5723M182.607 24.1556L181.329 16.4891C181.17 15.5496 180.653 14.7083 179.887 14.1413C179.121 13.5743 178.165 13.3255 177.22 13.447C176.275 13.5686 175.413 14.051 174.816 14.7933C174.218 15.5356 173.931 16.4803 174.014 17.4297L175.44 33.1139M189.774 27.7389V25.0514C189.774 24.1011 189.396 23.1896 188.724 22.5176C188.052 21.8456 187.141 21.4681 186.19 21.4681C185.24 21.4681 184.328 21.8456 183.656 22.5176C182.984 23.1896 182.607 24.1011 182.607 25.0514V31.3223" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M196.94 27.7389V24.1556C196.94 23.2052 196.563 22.2938 195.891 21.6218C195.219 20.9498 194.307 20.5723 193.357 20.5723C192.407 20.5723 191.495 20.9498 190.823 21.6218C190.151 22.2938 189.774 23.2052 189.774 24.1556V27.7389" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M202.315 33.1139C201.355 40.2806 196.299 43.8639 188.878 43.8639C181.457 43.8639 175.44 40.2806 175.44 33.1139" stroke="white" stroke-width="2"/>
                    <path d="M192.805 34.9056H187.982C187.032 34.9056 186.12 34.5281 185.448 33.8561C184.776 33.184 184.399 32.2726 184.399 31.3223C184.399 30.3719 184.776 29.4605 185.448 28.7885C186.12 28.1165 187.032 27.7389 187.982 27.7389H195.149C199.108 27.7389 203.211 31.3223 201.419 36.6973" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M90.2139 14.0215C90.2139 14.8418 90.1084 15.583 89.8975 16.2451C89.6865 16.9014 89.3906 17.4873 89.0098 18.0029C88.6348 18.5127 88.1865 18.9521 87.665 19.3213C87.1436 19.6904 86.5723 19.9951 85.9512 20.2354C85.3301 20.4697 84.668 20.6455 83.9648 20.7627C83.2676 20.874 82.5498 20.9297 81.8115 20.9297C81.5361 20.9297 81.2666 20.9238 81.0029 20.9121C80.7393 20.8945 80.4697 20.8711 80.1943 20.8418L80.4404 9.04688C81.085 8.8418 81.7471 8.69824 82.4268 8.61621C83.1123 8.52832 83.792 8.48438 84.4658 8.48438C85.3037 8.48438 86.0742 8.61035 86.7773 8.8623C87.4805 9.11426 88.0869 9.47754 88.5967 9.95215C89.1064 10.4268 89.502 11.0068 89.7832 11.6924C90.0703 12.3779 90.2139 13.1543 90.2139 14.0215ZM86.6104 14.584C86.6162 14.2676 86.5811 13.9629 86.5049 13.6699C86.4346 13.377 86.3145 13.1191 86.1445 12.8965C85.9805 12.668 85.7695 12.4863 85.5117 12.3516C85.2539 12.2109 84.9463 12.1348 84.5889 12.123L84.2373 17.5723C84.5889 17.5195 84.9082 17.4053 85.1953 17.2295C85.4824 17.0479 85.7285 16.8281 85.9336 16.5703C86.1445 16.3066 86.3057 16.0166 86.417 15.7002C86.5342 15.3779 86.5986 15.0469 86.6104 14.707V14.584ZM99.0732 8.32617C99.0381 8.87695 99.0059 9.42188 98.9766 9.96094C98.9473 10.5 98.9092 11.0449 98.8623 11.5957L95.1357 11.7891L95.0479 12.8965H97.667L97.4736 15.6211L94.8369 15.709L94.749 16.9922H96.9287H98.4756C98.4404 17.6367 98.4023 18.2783 98.3613 18.917C98.3262 19.5498 98.2939 20.1855 98.2646 20.8242L90.6885 21L90.9697 8.32617H99.0732ZM111.334 8.39648L110.701 20.3145L106.096 20.7363L103.635 14.3555L103.248 20.8594H99.293L99.6094 8.39648L104.004 8.18555L107.045 14.5137L107.186 8.53711L111.334 8.39648ZM122.804 8.67773L119.587 20.9121L115.228 21.1582L111.272 8.80078L115.438 8.41406L117.126 15.6211L118.761 8.41406L122.804 8.67773ZM131.417 8.32617C131.382 8.87695 131.35 9.42188 131.32 9.96094C131.291 10.5 131.253 11.0449 131.206 11.5957L127.479 11.7891L127.392 12.8965H130.011L129.817 15.6211L127.181 15.709L127.093 16.9922H129.272H130.819C130.784 17.6367 130.746 18.2783 130.705 18.917C130.67 19.5498 130.638 20.1855 130.608 20.8242L123.032 21L123.313 8.32617H131.417ZM142.025 12.5273C142.025 12.9844 141.984 13.4004 141.902 13.7754C141.826 14.1445 141.703 14.4844 141.533 14.7949C141.363 15.1055 141.144 15.3926 140.874 15.6562C140.604 15.9199 140.279 16.1719 139.898 16.4121L141.99 20.1387L138.035 20.9121L136.682 17.168L135.592 17.2031L135.434 20.8594H131.654C131.684 19.5234 131.71 18.1934 131.733 16.8691C131.763 15.5449 131.795 14.2148 131.83 12.8789C131.842 12.2051 131.854 11.5371 131.865 10.875C131.877 10.2129 131.9 9.54492 131.936 8.87109C132.346 8.71875 132.75 8.59277 133.148 8.49316C133.547 8.39355 133.945 8.31738 134.344 8.26465C134.748 8.20605 135.155 8.16797 135.565 8.15039C135.981 8.12695 136.406 8.11523 136.84 8.11523C137.508 8.11523 138.152 8.20898 138.773 8.39648C139.4 8.57812 139.954 8.85352 140.435 9.22266C140.915 9.5918 141.299 10.0518 141.586 10.6025C141.879 11.1533 142.025 11.7949 142.025 12.5273ZM138.088 12.8086C138.088 12.5625 138.053 12.3369 137.982 12.1318C137.918 11.9268 137.818 11.751 137.684 11.6045C137.555 11.4521 137.391 11.335 137.191 11.2529C136.998 11.165 136.77 11.1211 136.506 11.1211C136.389 11.1211 136.274 11.1299 136.163 11.1475C136.052 11.1592 135.943 11.1797 135.838 11.209L135.697 14.4785H135.908C136.16 14.4785 136.415 14.4463 136.673 14.3818C136.937 14.3174 137.171 14.2178 137.376 14.083C137.587 13.9482 137.757 13.7754 137.886 13.5645C138.021 13.3535 138.088 13.1016 138.088 12.8086ZM65.4619 25.1504L64.751 30.5078C64.5055 30.4401 64.2601 30.3936 64.0146 30.3682C63.7692 30.3428 63.5238 30.3301 63.2783 30.3301C62.652 30.3301 62.0553 30.4147 61.4883 30.584C60.9212 30.7448 60.4176 30.9945 59.9775 31.333C59.5459 31.6715 59.1989 32.0947 58.9365 32.6025C58.6826 33.1104 58.5557 33.707 58.5557 34.3926C58.5557 34.8327 58.6234 35.2135 58.7588 35.5352C58.9027 35.8568 59.1016 36.1234 59.3555 36.335C59.6094 36.5465 59.9098 36.7031 60.2568 36.8047C60.6038 36.9062 60.9847 36.957 61.3994 36.957C61.7126 36.957 62.0384 36.9232 62.377 36.8555C62.7155 36.7878 63.0498 36.6989 63.3799 36.5889C63.71 36.4788 64.0316 36.3519 64.3447 36.208C64.6579 36.0641 64.9456 35.916 65.208 35.7637L64.7002 41.7305C64.3701 41.8997 64.0104 42.0521 63.6211 42.1875C63.2402 42.3145 62.8467 42.4287 62.4404 42.5303C62.0342 42.6234 61.6279 42.6953 61.2217 42.7461C60.8154 42.7969 60.4261 42.8223 60.0537 42.8223C58.9788 42.8223 57.9759 42.6234 57.0449 42.2256C56.1139 41.8278 55.3057 41.2819 54.6201 40.5879C53.9346 39.8939 53.3929 39.0771 52.9951 38.1377C52.6058 37.1898 52.4111 36.1699 52.4111 35.0781C52.4111 33.6309 52.6185 32.2682 53.0332 30.9902C53.4479 29.7038 54.0573 28.5781 54.8613 27.6133C55.6654 26.6484 56.6598 25.8867 57.8447 25.3281C59.0381 24.7695 60.4092 24.4902 61.958 24.4902C62.542 24.4902 63.1387 24.5368 63.748 24.6299C64.3659 24.723 64.9372 24.8965 65.4619 25.1504ZM81.8008 34.0371C81.8008 34.8073 81.7119 35.5521 81.5342 36.2715C81.3564 36.9824 81.0983 37.651 80.7598 38.2773C80.4297 38.9036 80.0234 39.4792 79.541 40.0039C79.0671 40.5202 78.5296 40.9645 77.9287 41.3369C77.3363 41.7093 76.6888 42.0013 75.9863 42.2129C75.2839 42.416 74.5391 42.5176 73.752 42.5176C72.9902 42.5176 72.2624 42.4202 71.5684 42.2256C70.8828 42.0309 70.2396 41.7601 69.6387 41.4131C69.0378 41.0576 68.4919 40.6344 68.001 40.1436C67.5186 39.6442 67.1038 39.0941 66.7568 38.4932C66.4183 37.8838 66.1517 37.2321 65.957 36.5381C65.7708 35.8441 65.6777 35.1204 65.6777 34.3672C65.6777 33.6309 65.7666 32.9115 65.9443 32.209C66.1221 31.498 66.376 30.8294 66.7061 30.2031C67.0446 29.5768 67.4508 29.0013 67.9248 28.4766C68.3988 27.9518 68.9277 27.499 69.5117 27.1182C70.1042 26.7373 70.7432 26.4411 71.4287 26.2295C72.1143 26.0179 72.8379 25.9121 73.5996 25.9121C74.8268 25.9121 75.944 26.1025 76.9512 26.4834C77.9668 26.8643 78.8301 27.4102 79.541 28.1211C80.2604 28.8236 80.8148 29.6784 81.2041 30.6855C81.6019 31.6842 81.8008 32.8014 81.8008 34.0371ZM76.1641 34.3672C76.1641 34.0033 76.109 33.652 75.999 33.3135C75.8975 32.9665 75.7451 32.6618 75.542 32.3994C75.3389 32.1286 75.085 31.9128 74.7803 31.752C74.484 31.5827 74.1413 31.498 73.752 31.498C73.3542 31.498 72.9987 31.57 72.6855 31.7139C72.3724 31.8577 72.1016 32.0566 71.873 32.3105C71.653 32.556 71.4837 32.848 71.3652 33.1865C71.2467 33.5166 71.1875 33.8678 71.1875 34.2402C71.1875 34.5957 71.2383 34.9512 71.3398 35.3066C71.4414 35.6621 71.5938 35.9837 71.7969 36.2715C72 36.5592 72.2497 36.792 72.5459 36.9697C72.8506 37.1475 73.2018 37.2363 73.5996 37.2363C73.9974 37.2363 74.3529 37.1602 74.666 37.0078C74.9876 36.847 75.2585 36.6354 75.4785 36.373C75.6986 36.1022 75.8678 35.7933 75.9863 35.4463C76.1048 35.0993 76.1641 34.7396 76.1641 34.3672ZM99.9551 24.7949L99.041 42.0098L92.3887 42.6191L88.834 33.4023L88.2754 42.7969H82.5625L83.0195 24.7949L89.3672 24.4902L93.7598 33.6309L93.9629 24.998L99.9551 24.7949ZM113.45 25.1504L112.739 30.5078C112.494 30.4401 112.248 30.3936 112.003 30.3682C111.757 30.3428 111.512 30.3301 111.267 30.3301C110.64 30.3301 110.044 30.4147 109.477 30.584C108.91 30.7448 108.406 30.9945 107.966 31.333C107.534 31.6715 107.187 32.0947 106.925 32.6025C106.671 33.1104 106.544 33.707 106.544 34.3926C106.544 34.8327 106.612 35.2135 106.747 35.5352C106.891 35.8568 107.09 36.1234 107.344 36.335C107.598 36.5465 107.898 36.7031 108.245 36.8047C108.592 36.9062 108.973 36.957 109.388 36.957C109.701 36.957 110.027 36.9232 110.365 36.8555C110.704 36.7878 111.038 36.6989 111.368 36.5889C111.698 36.4788 112.02 36.3519 112.333 36.208C112.646 36.0641 112.934 35.916 113.196 35.7637L112.688 41.7305C112.358 41.8997 111.999 42.0521 111.609 42.1875C111.229 42.3145 110.835 42.4287 110.429 42.5303C110.022 42.6234 109.616 42.6953 109.21 42.7461C108.804 42.7969 108.414 42.8223 108.042 42.8223C106.967 42.8223 105.964 42.6234 105.033 42.2256C104.102 41.8278 103.294 41.2819 102.608 40.5879C101.923 39.8939 101.381 39.0771 100.983 38.1377C100.594 37.1898 100.399 36.1699 100.399 35.0781C100.399 33.6309 100.607 32.2682 101.021 30.9902C101.436 29.7038 102.046 28.5781 102.85 27.6133C103.654 26.6484 104.648 25.8867 105.833 25.3281C107.026 24.7695 108.397 24.4902 109.946 24.4902C110.53 24.4902 111.127 24.5368 111.736 24.6299C112.354 24.723 112.925 24.8965 113.45 25.1504ZM126.272 24.6934C126.222 25.4889 126.175 26.276 126.133 27.0547C126.09 27.8333 126.035 28.6204 125.968 29.416L120.585 29.6953L120.458 31.2949H124.241L123.962 35.2305L120.153 35.3574L120.026 37.2109H123.175H125.409C125.358 38.1419 125.303 39.0687 125.244 39.9912C125.193 40.9053 125.147 41.8236 125.104 42.7461L114.161 43L114.567 24.6934H126.272ZM141.596 30.7617C141.596 31.4219 141.536 32.0228 141.418 32.5645C141.308 33.0977 141.13 33.5885 140.885 34.0371C140.639 34.4857 140.322 34.9004 139.933 35.2812C139.543 35.6621 139.074 36.026 138.523 36.373L141.545 41.7559L135.832 42.873L133.877 37.4648L132.303 37.5156L132.074 42.7969H126.615C126.658 40.8672 126.696 38.946 126.729 37.0332C126.772 35.1204 126.818 33.1992 126.869 31.2695C126.886 30.2962 126.903 29.3314 126.92 28.375C126.937 27.4186 126.971 26.4538 127.021 25.4805C127.614 25.2604 128.198 25.0785 128.773 24.9346C129.349 24.7907 129.924 24.6807 130.5 24.6045C131.084 24.5199 131.672 24.4648 132.265 24.4395C132.866 24.4056 133.479 24.3887 134.105 24.3887C135.07 24.3887 136.001 24.5241 136.898 24.7949C137.804 25.0573 138.604 25.4551 139.298 25.9883C139.992 26.5215 140.546 27.1859 140.961 27.9814C141.384 28.777 141.596 29.7038 141.596 30.7617ZM135.908 31.168C135.908 30.8125 135.857 30.4867 135.756 30.1904C135.663 29.8942 135.519 29.6403 135.324 29.4287C135.138 29.2087 134.901 29.0394 134.613 28.9209C134.334 28.7939 134.004 28.7305 133.623 28.7305C133.454 28.7305 133.289 28.7432 133.128 28.7686C132.967 28.7855 132.811 28.8151 132.658 28.8574L132.455 33.5801H132.76C133.124 33.5801 133.492 33.5335 133.864 33.4404C134.245 33.3473 134.584 33.2035 134.88 33.0088C135.185 32.8141 135.43 32.5645 135.616 32.2598C135.811 31.9551 135.908 31.5911 135.908 31.168ZM155.903 24.8457L155.776 30.2285L151.993 30.3809L151.028 42.416L145.671 42.6953L145.696 30.6602L141.913 30.8633L142.065 24.8711L155.903 24.8457ZM169.602 36.2461C169.602 37.4056 169.398 38.4212 168.992 39.293C168.594 40.1562 168.044 40.8757 167.342 41.4512C166.648 42.0267 165.831 42.4583 164.892 42.7461C163.961 43.0339 162.958 43.1777 161.883 43.1777C161.468 43.1777 161.011 43.1227 160.512 43.0127C160.021 42.9027 159.521 42.7673 159.014 42.6064C158.506 42.4372 158.015 42.2594 157.541 42.0732C157.076 41.8786 156.661 41.6966 156.297 41.5273L156.855 36.2969C157.575 36.7285 158.37 37.0586 159.242 37.2871C160.122 37.5072 160.986 37.6172 161.832 37.6172C161.993 37.6172 162.188 37.613 162.416 37.6045C162.645 37.5876 162.86 37.5495 163.063 37.4902C163.275 37.4225 163.453 37.3252 163.597 37.1982C163.741 37.0713 163.812 36.8893 163.812 36.6523C163.812 36.4915 163.762 36.3561 163.66 36.2461C163.559 36.1276 163.427 36.0345 163.267 35.9668C163.106 35.8906 162.924 35.8356 162.721 35.8018C162.518 35.7594 162.319 35.7298 162.124 35.7129C161.929 35.696 161.747 35.6875 161.578 35.6875C161.409 35.6875 161.273 35.6875 161.172 35.6875C160.444 35.6875 159.78 35.5605 159.179 35.3066C158.586 35.0527 158.074 34.7015 157.643 34.2529C157.219 33.7959 156.889 33.2585 156.652 32.6406C156.415 32.0143 156.297 31.3372 156.297 30.6094C156.297 29.6107 156.496 28.7178 156.894 27.9307C157.3 27.1351 157.837 26.4622 158.506 25.9121C159.183 25.3535 159.957 24.9261 160.829 24.6299C161.701 24.3337 162.602 24.1855 163.533 24.1855C163.948 24.1855 164.375 24.2025 164.815 24.2363C165.256 24.2617 165.691 24.3125 166.123 24.3887C166.563 24.4648 166.991 24.5622 167.405 24.6807C167.82 24.7992 168.214 24.9473 168.586 25.125L168.104 30.2793C167.528 30.0846 166.923 29.9238 166.288 29.7969C165.662 29.6615 165.048 29.5938 164.447 29.5938C164.337 29.5938 164.193 29.598 164.016 29.6064C163.846 29.6064 163.664 29.6191 163.47 29.6445C163.284 29.6615 163.093 29.6911 162.898 29.7334C162.704 29.7757 162.53 29.835 162.378 29.9111C162.226 29.9788 162.103 30.0719 162.01 30.1904C161.917 30.3089 161.874 30.4486 161.883 30.6094C161.891 30.7956 161.959 30.9479 162.086 31.0664C162.221 31.1764 162.391 31.2653 162.594 31.333C162.805 31.3923 163.034 31.4346 163.279 31.46C163.533 31.4854 163.783 31.5023 164.028 31.5107C164.274 31.5107 164.502 31.5107 164.714 31.5107C164.925 31.5023 165.099 31.5065 165.234 31.5234C165.911 31.5658 166.521 31.7096 167.062 31.9551C167.604 32.2005 168.061 32.5264 168.434 32.9326C168.814 33.3389 169.102 33.8255 169.297 34.3926C169.5 34.9512 169.602 35.569 169.602 36.2461Z" fill="white"/>
                    <defs>
                    <clipPath id="clip0_0_1">
                    <rect width="49" height="49" fill="white" transform="translate(0 1)"/>
                    </clipPath>
                    </defs>
                </svg>
            </a>
        </nav>
        <main style="display: flex; background-color: #dedede; justify-content: center; align-items: center; padding: 24px;">
        <div style="width: 375px; border-radius: 15px; padding: 24px; border: 1px solid #ccc; background-color: #fff;">
    '''


def get_footer() -> str:
    """ Gets the footer content """
    return '</div></main></body></html>'


@app.route("/")
def main() -> str:
    """ Route: Web Application Homepage """
    return get_header('User Input') + '''
    <form action="/display-user-input" method="POST" style="display: flex; flex-direction: column; margin-block-end: 0;">
        <label for="user_feeling" style="font-size: 24px; margin-bottom: 16px; font-family: sans-serif;">👋 How are you feeling today?</label>
        <input type="text" name="user_feeling" id="user_feeling" placeholder="Good, bad, ready to rock, etc..." style="height: 36px; border-radius 40px; padding: 10px 20px; font-size: 24px;" />
        <input type="submit" value="✉️ SUBMIT" style="background: #080808; color: #fff; margin-top: 16px; height: 36px; border-radius: 40px; text-align: center; font-size: 24px; border: none;" />
     </form>
    ''' + get_footer()


@app.route("/display-user-input", methods=["POST"])
def echo_unput() -> str:
    """ Route: After User Input """
    input_text = request.form.get("user_feeling", "")
    if not input_text:
        input_text = "Nothing :-("
    return get_header('Response') + f'''
        <p style="font-size: 18px; margin-bottom: 16px; font-family: sans-serif; text-align: center; color: #666;">
            🔊 You said:
        </p>
        <p style="font-size: 24px; margin-bottom: 16px; font-family: sans-serif; text-align: center;">
            {input_text}
        </p>
        <p style="font-size: 18px; margin-bottom: 16px; font-family: sans-serif; text-align: center; color: #666;">
            👨‍🔧 Check back for an easier way to find <em>good</em> concerts in Denver, CO.
        </p>
        <p style="text-align: center;"><a href="/">Try Again</a></p>
    ''' + get_footer()
