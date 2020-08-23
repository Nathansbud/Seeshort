import requests
import base64

seesaw_icons = {
    ":mic:":"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAD0AAAA9BAMAAADsTHzaAAAAKlBMVEVHcEw1NTUzMzMyMjIzMzMzMzMvLy8zMzMvLy8zMzMzMzMyMjIyMjIzMzP/kanEAAAADnRSTlMAMIDA8P8gRxCQ1XBgo/Cv9B4AAAGESURBVHgBYsAGGJVdQ53VGHABdtNQEDDHIc0xNRQCZmCX7wqFgqgGrNqXhsLACkAfZQjTMBCF4X9A2CAsqahPDXizgK1YmMCw7UJoR1KBTw2+Ah8MCRYBegZfU49ZMu+9JtDL9b3+j04t+9Jv3929nsUPA3Yri3913G0N/VzwBfMDgV3O/FTyjPmR5K4gfqZ42ccFGsmT/uIflID4q/tWgoT+XAiYx85pQUlHowUFHY0SZP06pwU5bY0WLKhOC7ZUFwQ8H1NPvYDm6/yvOPYCms9x+8hoHgRvXJdVCIJLcF0KeMH4Aly3joDJrBUAXHcXXp8lAK6rgeMPkz/+/rjpNnEPo+7W1/HgT53Pa9ovpf3Spf5gPrmufW7X7n9FdepT05WgcAqzjq8VvhLMrR0pvOljPEu8joiruisM1t0TRiPtNQbr3jFYt6qYzwR/YXwi8A1jPHU4iwy+6/jewIgDXlrYDxzNFAlo6UpAM0WChIEUXJsoCLICGBLw0pUgH8SY/G//Ac7mECByBEbmAAAAAElFTkSuQmCC",
    ":label:":"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAD0AAAA9BAMAAADsTHzaAAAAElBMVEVHcEwzMzMzMzMyMjIzMzMzMzOk8eTJAAAABXRSTlMAQIDBKrEQatUAAAA2SURBVDjLY2BgUMIJHBhAIBQnEBiVp4K8MRxARBF8SPgjALIubGBUflR+VH5UflR+aMpjKfUBv5fLmZKkNngAAAAASUVORK5CYII=",
    ":move:":"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAD0AAAA9BAMAAADsTHzaAAAALVBMVEVHcEw1NTUzMzMyMjIvLy8zMzMzMzMzMzMzMzMzMzMvLy8yMjIzMzMyMjIyMjKbuTISAAAAD3RSTlMAMIBlEFCb//HVIMBATLA1wmI/AAABm0lEQVR4AWIAAkZlBwZUwKqKzEsHtFIHGnIDYQDHv71s09tcnAAtDnWwAKVIoSyoAg44gFU4gG33mn8iqxSaFyjRggM9gAWCpfYBos+wKH2NJje9nU53JoP2z4eZH+ZjV/hg8rjmiz4FkJseQqlPJ8DW8GPAcEvaj2xcGNscZGz8klV717MXraoub0QXs5C+U/JE3TRvxeIp7Ib8JyyGvPH7tcdX/+K1x/l/nv3pzyk3fUCxuQt+aI6xlGk/xZb5/3l93gWU531Tw0Og/7kjQO09gUJ7VKnX4r0/gKXovm6emi7fv13IQbG5ttVLGbeJyNlWjcUfk0nYTUBm9RqSR7C9hQuLR8CTaTcpzE0Peo+BXQPraTemH937+i+Pk73nFh/V5ezesfgJfPJ4MRt25k5X98sBHwH5jUjocKmAtXqHM4tfAUvltNpZ/PZL9YDTjwF2yj8D74GPlfYQ4J1ynfYRQDFzutQAc7enAG8mTn8FUD50eghA6vQIgMrp0qCz+aXHJx4PPD6uhl2uPH5r82vPN2qlPfa41A7/BXUa4QSWaj7LAAAAAElFTkSuQmCC",
    ":add:":"https://files.seesaw.me/release/prod/images/shortcuts/addresponse_green@3x.8b9b598c7d2b7596.png",
    ":seesaw:":"https://files.seesaw.me/release/prod/images/shortcuts/seesaw3x.d2d87ffd62e6bc00.png",
    ":pencil:":"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAD0AAAA9BAMAAADsTHzaAAAAIVBMVEVHcEwvLy8vLy8zMzMzMzMzMzMzMzMzMzMyMjIzMzMyMjJuq9KpAAAAC3RSTlMAECDgoP+A8MBCYD0qhN0AAAEoSURBVHgBfNIlQ4RBFIXhg0vahBU841pw+sq7VnCoaMYt4Zbw34kNDvee9Ok8I0c/kyM/9fIzMi4vuSzISz5JeWkkFXF5GHd5WHB5SLg8UOPy0O/yEHN5SPs8HLo8rLk8ZFwe0jafujoBDk0+qVKg2dv8Dsia/Lh0BnGTj0jFwI3JSyVAs81L25C0eeksOAYfJjBu8gqQzYcvTT5I1Jh8+LTf5AMV85o/Awmbl8qBGpOXCoE1k5dyViBj8mECaZuX8oBDk5dKgTWTl9QBGZuXHiFu82ECNyavUDKTDyXLWvyfkgW+ZPTj8+GaHyULfNU2veF2jvRtCbDwnW9YAfYl6QRITX5vOZAGgEHpeRoQlilQEVweARLZShEcLPLhQH2Y8siAqvKj8gATuuOMt6I0aQAAAABJRU5ErkJggg==",
    ":photo:":"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAD0AAAA9BAMAAADsTHzaAAAAKlBMVEVHcEwyMjIyMjIzMzMvLy8zMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMyMjKq3jkmAAAADnRSTlMAWcCiECr/gJBA0PDgcJsQ6wUAAAFnSURBVHgB5NCBRwNhGMfx37W7tpVxyCA4lwaFQSPgBFJwxEKwNT1tu0XBhoLIApiwiRAyAImdIBYagP6k6nZ6373P3SUC+gLeD8/7ePBf0mzRisO9TFIW97bsFe5d2RvcCzFu3E4byl4PH10gTwnVAJ+SckGJ9UDUsj/zY326bP4H79NXT9ed9Xj3NgBgfxI3/wpBOT96vzdgYNuXDrZmPazp6OfBTVyUovwBdxT0glSEe45GYUUUuFfFCWrY5W4Z9N17jntvQfgIE9Wb8oVraKt+gpJwzymrfqSTlLmoeiUr++mc6vc52a2M6lZ6xtO/9UdN9mKK7Wck79eAL7k7r3pdvk8LedVbKAuvoqQ6mRnhY4OYj/Wh+D7F/RgHYnyfO5lGOMAzdT/CR9imoFXsUIR7JvZ8ItqEMYxyqjswBmc9YJkinV4RdEMxTs9LQPaCmIsO14i48/7Ou0ncBLROQh+7wjDUAQDo/Q33kx+9fAAAAABJRU5ErkJggg==",
    ":3dots:":"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADwAAAA9BAMAAAADjhfkAAAAElBMVEVHcEwvLy8zMzMzMzMzMzM1NTUBjgFqAAAABnRSTlMAHqDw/zD8JIl5AAAAX0lEQVR4AWMYEWAUjAIhE2dF3GxWExcX5wAQHytb2AUIDMEi2NgqIMoJLIKNbQKinMEi2NguYCAAFsJkwygwwGQTMJyA0wh4jFCwMAi5uEADEjubUQDCx8IeEWAUjAIAs+8v8UtVCQMAAAAASUVORK5CYII=",
    ":pen:":"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAD0AAAA9BAMAAADsTHzaAAAALVBMVEVHcEwvLy8yMjIyMjIzMzMzMzMzMzMzMzMyMjIxMTEzMzMzMzMzMzMzMzMzMzPjbCdaAAAAD3RSTlMAELHAkID/QGQl0ODwT6BXFUFmAAABWklEQVR4AXyTL0xCURjFAf/LdCSTgc3NTHBuNpOZGczqgx8wnsyEFjcSm41ENplJFJKFbKdYpPekbte7++477/vFd972fd8555YylE/OShZb8GjpFRhZ+gY0LX0b6pY+hTdLH8KtpY+hZ+k30LH0c2hb+hxalg4khrwHpIZ+AGDHYwX0fL345fu1QF7huJDyLv+kE+2950N75+nq2z19oR9C8vTHy1yW7Ah6PsSGjLYR/imiG/lJA3V9P9i0JprdDi5tiubeBS2cxfoavkqOat6hMjAJdkni5MNP5WWuBVV4UMP0StOcQ+8wUsc6diCtZXqaxuENtNl64Ni/cx3pcfROl/Cp50XhBREGJd7PGX6aiXDoK62/rOEy53dXTNMbbcJ9oPkIxbWeK6iL8KSj6sFUoCXDCz/Gv+pGTEEz86tqOv5UTeKsKmTirNa4kq8WhcxclEX8LGHg5QHFnRO4bDxg2AAAAABJRU5ErkJggg==",
    ":video:":"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAD0AAAA9BAMAAADsTHzaAAAALVBMVEVHcEw1NTUzMzMvLy8vLy8zMzMzMzMzMzMzMzMzMzMzMzMyMjIyMjIyMjIyMjIXVtRYAAAAD3RSTlMAMEAgEIDY//BQm3DAsGB1azhNAAABdklEQVR4Ae3VAeQTYRjH8Wf/vTWzloEtgRkcwAEmcNJSBUNaEUIcgVG771kHFQ5gkESIYkMyEBADjgyHAmAYKQIAIJ2we173whjoB/DxeF733Pu8ctLUBr6LRyHRHUd1CkSdSr8EwHOxc/W+L2LCwqPA4lswD6RFEdaai8KXch5m1ybwUPsFgEgaMJZzMNXeI3kACw86cgZPtE/IZcm73j9/antfPDYNyKUNU9t38pq8DcmbDHLtP3hRC1lfpAg77TcA8CUDIBGdovCZyPXCH4nYDWAsYjIgCbSan/WP0fvadvvtbMXj/mih+B4fRMwE4t3fZmlcHkAX4u+vVgDRp8GvVLUwIVY2B97Gzqw0HDvxQYOlMv0JQ1tLIwCqDtjM5i6/HYJf7VdSoF/pb8Hln3F6C7cPcbv334/yIcfNR+7idrmcul2aK7eL+U3k/v9v7vX9sVeshx0CtVwd99ekCvWK6irUL4DRJ4zHUkr9y/YwX/dywvwBqK8hKvEtOBwAAAAASUVORK5CYII=",
    ":background:":"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAD0AAAA9BAMAAADsTHzaAAAAMFBMVEVHcEwvLy8zMzMyMjIyMjI0NDQvLy8yMjIzMzMyMjIyMjIzMzMzMzMzMzMzMzMzMzOjmfY3AAAAEHRSTlMAIEBxXy8QToCvwNX/oPCQi6lVDAAAAb5JREFUeAFiQAZCJkAC0Cw9wNwNxQEUP7Nt245mxbOD2VY42/aC2bYRzu1/jDNbjZ2xN+lLee+b9/2Ch1Nc9UJjxJKDe2CMWI0weCQipwaiJcoLdDKLcitNt9DJJsptqEiyy6pfhX74sh70bISOqh+H3HvDc0o9N5/7cacrZL80EE+Og4H7aSVyH2DcapJVrg7KIDKkTE0WgTJ5cVeAsuJ7Ddk3i5wE6CNyA+BzoN+CMepzImRzRGyAJot9C2G56m8gj/rsSozj7c909XlPs/+3vec803TL69d058PrN/Xv76s5h8tT58O7/7AEXPXPRyb1oLNwOdjvAitF9gCMcn8OhMVBDYHsNduCUmLuQH5f5aBqkK1yEEiQBR0lqCKXI/2wBBXkcLSfrFy5ju0+Wh5UrtwCPkf7dshtATIb6kALU68FfU29JuQ39WqQz9QrQg7T+N2OY5i/6p/13QYoq39+dYB8hvEpmRxzZ3mansfc1QuMnemhfn7x4mW2e1ZlH54syfPfTsqjpG4PJCVf0vvP4uuY0IMyO+bOqDSdaWk6HYL9JXHtvf7h4MF1A0lQZKvqm8VagEbh+TC0EkHfAU6VVoiYEWJ2AAAAAElFTkSuQmCC",
    ":highlighter:":"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAD0AAAA9BAMAAADsTHzaAAAALVBMVEVHcEwvLy8zMzMyMjIzMzMzMzMzMzMzMzMzMzMyMjI1NTUzMzMzMzMzMzMyMjIIFefjAAAAD3RSTlMAFlCw/4DgQKBmMPDQkMDyy+/EAAABWklEQVR4AeSTJVwuQRRHd9/DXQtu/Yd17I+7ZTRRcHdJuFc04bIdTRS0o703dHa+uWtY5JSVM3ZlJANkyZJ/8ZbavxpWug2w8PI8rLzLCKy88ymsfLACK+8BWHq7P+3/lQoU6StTDZEarQ8EIc1L42dBmdT4J1D6rD3u9L6V02ToSSZ+6w+pdlQ0Ps9LFz7xOCONDZ3PXtRMTxWKcQqgQvhWgDRxvD2APInjBiBGElknJSgBMgTJVtzll1bRxSutClPsgWwSLotI/ecAZEpaqoFJ21rlOh9l27MEKNB5ByDJVhsvnXcHktmrgjRJhyPPqAykUEf/8pEUnmFnEh7nFGk8PelU0Y7yABIN/A3gpVZvx8CXAHX6biU9E6am98LANwEF9IXiBxTQjSh82yGSfo6r6vnVpHSpYSswhnkZpmSx8piRzspjRiYrjxmprNHMeJkHOPrw6CcsDwDiU9PizS9N4QAAAABJRU5ErkJggg==",
    ":drawing:":"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAD0AAAA9BAMAAADsTHzaAAAAKlBMVEVHcEwzMzMzMzMyMjIvLy8zMzMzMzMzMzMvLy8zMzMyMjIzMzM1NTUyMjJmAb8JAAAADnRSTlMASoVgIPD/zxDgsKAwcCB0r60AAAFOSURBVHgBYiALMCopO+CRZgJ0UwcczYVhGMevvTtvO+2EwAAMGoDAUBAIQMSE4Nh2rbWiYIIYUQAD6xs8AAIHgn2I9Hkal63Rfd8I0AVj2+/PdjxPjxz5X8inJHkOby/kayIPfX6PvMO+y0czoG4GxB+wWpf9gCvgcgVKlyswnFn8AlgH2gbnBNCanBucfINW48DgWwGWFt8EcpYGV0D9K5OvAw3OTb4OVGzbXIGC45nNFah4aXMFCg6XJlcg5uR7wLWQ80/xRsxRxbxgzJ9jjm7MkcYhz3mbXK5z0go4Ct7tBhz/2c6OFy5Hi0sgSx5HZ7z9I39wLCbff5JxKe2x3Dwj6076xzO92BwNHdcs2Ryn1JvZgcnxSR3Tp2RyTK+xWn5Em+fsC5OjfePzOgfCfDyBsSZvhD9gbodDF+vpeFirXKz1IgzUQgzUhX+7LydoEBlENzcvAAAAAElFTkSuQmCC",
    ":shapes:":"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAD0AAAA9BAMAAADsTHzaAAAAKlBMVEVHcEwzMzMzMzMyMjIzMzMzMzMzMzMvLy8yMjIyMjIzMzMyMjIyMjIzMzNXWjrbAAAADnRSTlMAQIBf/+DwEMBw0CiwoBUDOm8AAAHJSURBVHgBlJSBRwNxFMdvW3PljLRLBZROwXDLAqCt752ZIhohgBgGFwaBYoAgIAE4ApgIgCyIYIhA/0ve73e7t3fd/egL9nz33nuf9/PO+pfWdox2BfBNfhUYmPwWcGzy+0Bgbm8coEr+mbG9cYA++YG5PeAb2gd9GsBAb9oA5VINQ3u/UjzAskotHsBVrYsGsLdiylQQD5OMeX3wAdL2fAn3uxupWW+MoRVGikKrO20q+xWpOnoLqYaaOtUFxTccBxRzeBqpQb+QapL6NFIytUPDalGCB6A3bUYCtt6IqSD9rpFPLsuZWTb5MxVRv2fh19o0JaXnF3B7nJ4UuFz0x3jS6VwgnMiHTtK5wJD9EcDpOQU8Ts8r4FyB07nAyWLA6VwgmtORHVpCZQCrKV3OlcTaZ7qB9AEIOnSEXeKz8Pjtxcq6TKf0lpmvw3RK7czt0FXYj+/u3O/J06b/23tgCcIl4MiyDsGShC7d1jp7WcIWcLvJFhMy9I80JeEYWUnCZCmBBxaY0IZS6Is6TFjS9n4F+YQrIH1bowLCMkWfhJFPSHXv6O2KCGOc09sVEzp6yywmNG3J//t9L3xDQceErJffKWECBkIAAFiq7bbY/NFhAAAAAElFTkSuQmCC",
    ":glowpen:":"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAD0AAAA9CAMAAAApvJHbAAAAn1BMVEVHcExTU1MzMzMzMzOOjo4vLy8zMzMyMjIvLy81NTU+Pj6UlJQzMzMyMjIzMzMyMjKAgIAzMzMzMzORkZF2dnY1NTUyMjKAgID///9KSkqAgIDu7u5GRkZhYWHn5+dWVlb///8zMzP////y8vJPT09zc3O/v7+dnZ1WVlbV1dX19fX29vb5+fnd3d2hoaHT09OysrIyMjLKysqwsLDQ0NBk+p0RAAAANXRSTlMAvlD/nxCAYCDi/iigwEBwzvGQY+8w+PX/60Va2fZx/xDQ4P/U/cnsc540RSGH////sLTboGbVgCwAAAI9SURBVHgBxZZnYyIhEIa5fQ8s2w5j7713/f+/7XBDyihMTH++JCrPDgzgq7ibP+ITBPj7TkMGSqlcXlwooBi+x81HeCROhEgB/HvPVDWeKT1oGB7ulnN4jQbKQOHeuVeIXEW1Vjd6o8k5ref/YiqjXa/XO4BmJt/t9R2lNYCBHNbrI1MdY2/5Cab2P0VclMyT64YZDPHcKS8ALK8nXq0CiKRYXewaLtWdvevC0FsS264aA7k2M28AaLtnvgGK24tObesPZCZr93FdzYy8q+8BTNfEtvqhftlwd+EjDDu7st6K2FbvANXEu1nGGmW1ZytBbaujqoSP/tToWwAbITz2QTBMbc8rykXBlM5JRj8B6MoYfnTgt/s9nMQAHDrv1xdYB+CJmOIbocATC4YvsdPEweBeOxEO4t+2B5KRKwPeNnrFL2u8ZUNXeJm3gYCXI+fi5AFMdVkgV4EJp4Lj6fbRgzwTjAMAzpueWFkKBmn1xN0ULfmUkpoed1o6YVKKGRfx17c/wcIOdK0cGd6OnZ9TKo8MssLA2UuaUpP+q70Jbm9Hjig0pSY2pWwhddtxyaVUDcDUlJe3XS/AUOBTqpOllB07IE1jrv6GppSd582PnBKfUuhtXu2ZvG55+mZKub9/7Bt8SrXs/+n14MieFT6lLAnZMtIIJqVokxTfckp/4R0tyTllITZdCQ9dpxaCdDHgHW+XSo7sY7jaoRh4Pwm5I+8lR5r4XhRp+XspkTvyXmJyyt9Lgdyw9xJ/1v4PSHQ0gL9G3i8AAAAASUVORK5CYII=",
    ":upload:":"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAD0AAAA9BAMAAADsTHzaAAAALVBMVEVHcEw1NTUzMzMzMzMzMzMzMzMzMzMyMjIyMjIvLy8yMjIyMjIzMzMzMzMvLy8rBGkIAAAAD3RSTlMAMEBQoO3/wGAQerDQkCDs2Vw6AAABUElEQVR4AdyUJUIFQBCGB3dJVNxdb4E7Cf1xdyeR0YIX7ABIpGCNgnX8ErjM7uw++vvqtzpGzoRLREQY2ckqAzA0Y9PZ+KTKopfxzblR+5z8+IZgk1/BL4UmP/Dn22ak9gXjQvpF7ptmhN+Cwnia5sug0rCraFfoNGyozxO0BTPvDkkx814wMPWPr7N5kYiXfpg4+taxMNPypR9hoeEzzm5lsPEZo2lYKZChFT+8h516pXAkbeJ47a165PK0RAbTg3Kf/pswtbDOiQI0v6/Ha1/1J9AaY0X1oiAC+RdmSKYrhF1I3Nd+eU/80kpUxr070S33LUp42yP2icYycvBLB9EVOFo6uohyHPkwIg8HvlF0lupriMinzO43eOdL3ypbJ5jH45wPti+KE9nrZsRkg2lK+ewD9va3NVAVm2HeJ0IfzhDjbXxW7uXIYJUCwzABAK2ZtfwUtkOtAAAAAElFTkSuQmCC",
    ":caption:":"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAD0AAAA9BAMAAADsTHzaAAAALVBMVEVHcEwzMzMyMjIyMjIyMjIvLy8zMzMvLy8zMzMzMzMzMzMyMjI1NTUzMzMzMzOhpmHAAAAAD3RSTlMAUHylwCCQEPD/QGAw0OB+W65DAAABo0lEQVR4AWIYEUDIxEURmR+U4gIopw44GoqiOICftbbHNglQQEgaMEEeEJABA9hHCHgMgqggT0N7e8te2+YhCBiBgAECMyD7BNm3qHvv7v3fc0QB0AF+/q97z+49t5OWU3CcfddtZE3PymluuZfpurfuGKeRYTnbVMO4Fm/cNQ5t3jd+tx7OFauZqwPlYOV8p3yJfKy8BesFL+BUuQ1nOVEQc1Pd8xlRATK/YOV5gF+n64Eo8J0QbfvuEVV8T0SeiDwTeSrz+S95TkWRl0ReFTmteR7IPGQ5dyLONxMeEbGGprgvd4GlWFxgE75W3uf70RXcEAMzID4Bu9oL56V2pYl2MO+qZpuJPYyxnfrgdaU9dE9iB/NI6CFxfsP8/vR9EGN7XXVsjyf0ZODOKHV+8d8X2aEZu+XX6BbLo52iWL7Glufd48Q/+ed9chXi9eKFLg3cjfcszYOeRGK7Gd/tQ5zt6K9/vhBnU9buWhZiflNBqJdTzWN4hjnx5U6dm4rnxK/iBm67/4w4636L+TEC1fuc5r5jfG0ams6Yj3hMHcT/oL4AJ73pn7yJixMAAAAASUVORK5CYII=",
    ":eraser:":"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAD0AAAA9BAMAAADsTHzaAAAAJ1BMVEVHcEwvLy8zMzMyMjIyMjIzMzMzMzMyMjIzMzMzMzMzMzMzMzMzMzM8zRkjAAAADXRSTlMAEEBlsPD/wCqAl9VQPVeMeQAAALtJREFUeAHt0CVixEAYQOGQKZgyM9gyyLItgy29MoMtnKCqNyiuzxH2Wst/OHGrdp4Z+IKjudX3l+rTImpYBulkNsRtO3i7D7ApLM37WP8m0PGr1zsItef1Z0h6QDXA+aws31MA664P59n7wingyF3acDzq+14b6JVVLXDgonzwrSwsYNTv+g6cyqIZLrRA03Au8zQcBr0GTmT+CWtBrwZkvgK3QTeAV/f0PoKuyw8GXaokVx6u7K5cufIsjLqRRYXZfJQAAAAASUVORK5CYII=",
    ":note:":"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAD0AAAA9BAMAAADsTHzaAAAAKlBMVEVHcEwyMjIzMzMzMzMyMjIyMjIvLy8zMzMzMzMyMjIyMjIzMzMzMzMzMzPaiT6zAAAADnRSTlMAV4FAcCgQ/+CwwPCg0D8IW1sAAAEMSURBVHgB7dKBRwNxFMDxt02hhQkQOElT4CgOYEAIMrgIJv0B7dZ8t10H4ACSJoBDLFMIdQAB+w/q38nj4u45cgRHX9w7Ph78PPlpq6Pf1q5o/T0xtRjq8OnpiKfWmwQ6PBIdUMXPKC3sZf5AeePMF5Q3+kMPmQDEpKC/qfE7gi7MPB6BN/CN9wnaMPRIYnBg03iD6w248nEW4KZR0/jpgdOGUfN5oPvbc7t/K3IMM5EG8C5ybvxmcAEwlxMgcluxcSZoxGhhinFb3Txa5nuyzofkW/+y3pFCK+vBTr792r3P62G+I+u4Uqhr/bPAa2m97+Pll/uQVVWfVryP+vu/j/PHUFKS+eWytHu1b5XVeD+9h6TkAAAAAElFTkSuQmCC",
    ":undo:":"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAD0AAAA9BAMAAADsTHzaAAAALVBMVEVHcEw1NTUzMzMvLy8yMjIzMzMzMzMzMzMyMjIzMzMzMzMvLy8zMzMzMzMyMjKmmJUjAAAAD3RSTlMAMEAQwP/w0KWQgCDgUGXaQViwAAABUElEQVR4AeyUAUd7YRSH3/33xzSbgREw9AESKoTQBaCyZ223W1x5AYgMgJEBYh8gECMDgz5BBiiBAIzc75Fwu+e89zoIgR7g3eN33vNu58x9U+s5i3o06Fh+DyZWfAyHdpyJHT/btuM3P43/xUcLycNS+iklkrtCN6nitRgrKnlxORGV3Oa+CyRHghUASSdvYAx6NHfuAVL5wNQpthCZ+leBYPjfgWdZ4DLcBuirr2jtFA35UUMUEJkrVWCm/QHELmcDGGr/DwbFr5qV12cqe2qXCzypRFbq4D8ci+t8uL9tOBXHbuibEItjzQ/enMIzUvU+nCai7zS/61cMLV2H2PItuLB8A84tvwvXlp/D2tBND0v7evN5md1eG5jZ8cT409kHTozqHut1mz5YqNZC8BhBEJ9TItWjGDJUzRPS74W7pvjcyQ1o3nVBBp4PGYgGAPH5vXD0p2EXAAAAAElFTkSuQmCC",
    ":arrow:":"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAD0AAAA9BAMAAADsTHzaAAAAJFBMVEVHcEwzMzMzMzMzMzM1NTUzMzMyMjIzMzMzMzMyMjIvLy8vLy9gGXonAAAADHRSTlMA1//wMEBjgaC6ECCZamOYAAABAklEQVR4AYzTIa4CMRSF4XmiL3l2zEsG1dOkdAGDQXUJLKFhBWMIdpaARnWphFB778+1n/nFPdN3N6fqcZBW8NR8VwZXA8/g2sALuHbwAq4neOy+awGP3XcdwFP1XSt4qr7rBK4GnsHVwDO4dvACrh28gGsBj913LeARXA38AX6x/P/+vttk+Rn+4wieuu/aLE9XI2D4+mcEfDzVXysgjOXMRkAYw7ECwhjejxEQxu6sgNdg5TOXEfYMwm0EzbZFYHkBDAs8qiH0YiX8JS07WuLCsAiWuHCBJqgDcIFNBBzAgccBiJjEU5tNAklXMeAEQfilGYBppJsBD2ADSuMF1Sg8AFUAZKQiRu9KAAAAAElFTkSuQmCC",
    ":link:":"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAD0AAAA9BAMAAADsTHzaAAAALVBMVEVHcEwvLy8zMzMzMzMyMjIzMzMyMjIvLy8zMzMyMjIzMzMzMzMzMzM1NTUyMjIc4WpEAAAAD3RSTlMAEFCAwJBgIECn/9jwMHC+XtboAAAB5UlEQVR4AX2TNbAVQRBFL+7ubhkJGv0Ed3dJcE1wTXBNcHeHu4v7JFg20Utx4k+eU8v2VE1DvzlPu7rOjnQ3LNoOHT1mFapyhAWvUIXNLHkDk4aewnRYrCWzuYf7OfKBqZNZbwAtLpLHbX0gCup6PjL1u/L3G/P1lr5Y/rYgj9u6UMN7ti4046OUjpbMUjoakbYe8KyofP+gCxO5W+VrlG7lFyfz+wZDQeoLbHFYh6Ta/SUyP9saCDRQFW7nWfCpNQLd4+02diz5iMBFflBXx3xS3FYNpRNCwJNA48vkg2Awbx3r54rfOgvJX8G4b9x8Q8+HulYSLJ1QPu0obwdD6V9kNy3J3Ya++CiHh1s/bug4yveQBW4YOpqG7TbjTUNHk3DwJrxl6GhI6aZ6vGXogONTKetdQy9+ZYF9Ky0d9SkPQG2sfwlBHcf877/9sQ4XDSzzmZXOvxnrDUO9gBaOQqQ3420EOkg6i8bmSzzEO8r0YjUTw6Oo42mfnaroGfmFFI56hpaPhoL8d8ST+bX/51tr/W5qfVU4GaKBKR21fJLSsdOakoj6zFondDQmjxt6vMEHti50J8dJdS0dLTzzeUXpnKFLW/HtkNm0dNVWeW+Y1PNl/hyq0NORzOahKnX2DRlcgcUfcF42PhqZxlcAAAAASUVORK5CYII=",
    ":redo:":"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAD0AAAA9BAMAAADsTHzaAAAAKlBMVEVHcEw1NTUzMzMzMzMyMjIzMzMzMzMzMzMzMzMyMjIvLy8zMzMyMjIvLy/jmlwSAAAADnRSTlMAMPD/YdhEgJDAEKCwIOWlLlsAAAFOSURBVHgB7JO1WsVAEIUXd38AtMQP7tLi6WhwKHEocVq0x2tc29vRYA+E3iQ7mf0mSMvfRM7u+CgTyUoktbhB1C2UiDoA0UA2ZAPNPgbC8QsD/wYiR2Y1pj0GQlbA6XX9WTCwLsvICMqxWzAyZk8cjJTuBiPP/vhYJWP7caU7+J4GoLKX1ke7HpINlPby8twF348A3PPyVtsfSx/v/PqJXbngu0acfj0GqFSUc705L0Aev16iHx4jcmyA9DYbxcFEtXxy3LYDFYqwBRS7tYwCitj+Zrpf8R9tJJDrH+mte7Pr1L7CvOGryGUl6pS/6hHAvKTT+DnRQJWkh/ssYgJtP8cCHuVNlgPc9wkgivSLE2uRfnMGfAxEk3kzEACwIehHALBNh5gNPCqvZzVaaQQMGvHbUjEVHECxogizbEN1gitm2YUKrnSilIEWDEQBAOu8f8A0jApCAAAAAElFTkSuQmCC",
    ":pause:":"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAD0AAAA9BAMAAADsTHzaAAAALVBMVEVHcEzPAADVAADVAQHVAQHUAQHUAADUAQHVAQHVAQHWAADUAADUAQHUAQHXAABCFX8cAAAAD3RSTlMAEFCAmcA64P/QcGDwsCDi4bVnAAABh0lEQVR4AbTUgccTYRzA8e/V683b2ztHoghLEOA4sQiROMDQMcAiDBApB6C27be6ZSM5wIACDCGEghwBgQEG6M8o3c96dvfcD3i/MHz2PPfcj3twCm4/StP04RP8Pc2k6v3Qo8FH2TffNPm+OOURtb7KQbPaI65JrUWI03Ep9V7i9EUa5V32nYqnt63LtY25XGSKNvJ7vtPRZOJvWfmZtPS6dXutGqJuv4jje/K3SRzfVe+7p+9DUIrIM6Bw3uCSegQMdFFP/jXR4fhdDzAw/AF0xPBvcNnyV3Bm+RiuWD6HkeUCd0wf0jO9i+0RW9sZnLMntmOff80nez7Y891x3fIcTixfwJHlb+CC5e+A0vAlkBi+Bn63ex4CR44X6onzAXfUf+inOP1/nX0H5wAv0kx/C2dLuCktzQB0AtYFlbR4pH7i5zFaUHh9hcYNH89DzA1W1vUvMg5x6jV8jdtxVuMPHHaxFLef1Lvq/uF5SKPT7Z5/4Sv4XL3m41u09WfPkszSHqCIAAC1XYz9Z9HgYAAAAABJRU5ErkJggg==",
    ":cameraroll:":"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAD0AAAA9BAMAAADsTHzaAAAAJFBMVEVHcEwzMzMzMzMyMjIyMjIzMzMzMzMvLy8xMTEzMzMzMzMzMzMqD03WAAAADHRSTlMAQJvAYv/QECWA6VBIfUqZAAAA3klEQVR4Ae3TgUbAUBTG8bMZRTCpN2hEMLZRwEQhwPKNBsAMYI9wVQEQQQNIoxcIerrOnZa13XMkMdifC34uHD5avf1ELGX2odQQXWh+TVRDyxBw1kkBIdkn5fbNb/tU8wBArPgD+43iEXuleAYu/LtH1kn2Q+ZCcZ+9UZw+8NL+8/3vn5IjI/rOJbgyl/wKQ1Xu9jt8VRqXez3Gitbh04m+Lf0A0x4XHv3w0sx91us3e07H6ciZ23E88B6z23FCtHveQ3RU9q/iwOa/9Fr1lt41LogCzWO7nE7smVbvE1wFSB4aaC9bAAAAAElFTkSuQmCC",
    ":check:":"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADwAAAA8CAMAAAANIilAAAAAP1BMVEVHcEx01GR00WR00mR00WR10mV002V00mRvz1910WV10WV3z2eA1nG46bDd9Nmn453p+Ob////M7sb3/PaQ24QjeWXgAAAADHRSTlMAMHCbyP9I8BCA4CAtBFsUAAABcElEQVR4AaXXVZLmMAwEYFObwnD/q+4O+E+5FJAy7vcv2CZ1HW2sQ4mzRitxvA0gCdZLZEwZl8kpcjYF3CakR+ozHpP9LY0WbGy8tp2DIK67sjpAlKB5y2veSnTHWKK72kaHV3GxwhYvY6tu4HX8gfN7nI8+4w8pPY8BkvTDOE44EuKbG8/LVwZ66yyy6/Kdmby1l9uvkA9uJXYqdiT/Oryw216XVCkNPvtSMqGOVkZgt0sLI3jl/mOHU8Eda+diV5A49cbSKOkPnns55i2Ph2K3Hjzmy8FjYpcdLB62Zdyvy8HigTwga1GVZF5+9MT/4KMkluByI4GFVYb+0qLHzw/GbYzS5yIuK1OOEl1PBv16aIkNZBo69FEOZsnxIFpo4U9T71DjiV9wEq2kyCKV5eZar482xMuFbt8EFulmid1n3ub7xX0aen5xb99WtG5omrZSbZs4Xss3n7xt3zI3b9bbjwntBxT50aj9UNZ0HPwPE31Kl1WGSqEAAAAASUVORK5CYII=",
    ":draft:":"https://files.seesaw.me/release/prod/images/shortcuts/draft_shortcut@3x.731030430755bb70.png",
    ":addpage:":"https://files.seesaw.me/release/prod/images/shortcuts/add_page_shortcut@3x.42b452210c7a64f3.png",
    ":pages:":"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAD0AAAA9CAYAAAAeYmHpAAAACXBIWXMAACE3AAAhNwEzWJ96AAABh0lEQVRoge2b0W2DQAyG/1Z9bzYoI+TB7+0I2QC6QTZoR+gGhQ26QTOAh6AbtBMQER1RKx8njpDCYX9SePAhxCdy5gzmpmkaaONWnTGAu3ZDRBsAHwAexR7LpwKwZ+bvoWfaXelUhVtyAK8iGqCTTlW4YyciAdYypx9EJIDeRNbDF4DaPzQrWwD315IumTkqQfwHRHS4NAep/HubtBZMWgsmrYXQfboXV5Vt+8avzMZ3eCJ6EsG/1Mx8WmxFSxNRAeBdDMzP54Bzr5i5iJImomyhwkPJ2xVd7JzORCQ9MsveWhiVvT1UCy1DX0RkQum2DD2I6MwQkVfa5rQWTFoLJq0Fk9aCSWvBpLVg0loIlZaZ5wnjXE9AJyUknbvf6rA5rYVO+kej9F6MrJhTImPm0vVy7PreFTmyNSS3c/Z2L7fexB6/cLew5KUte2vBpLVg0lqw0vICCk8Zulimkk5qwWJzWgux0ktssYiljpJ2RcmzGEiHtnmuHPXZ4cxtkmM5t0nq+9YSwBEvYkzgE72ZuwAAAABJRU5ErkJggg==",
    ":plus:":"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADwAAAA8BAMAAADI0sRBAAAAMFBMVEVHcEx01GR10WV00mR00WR10mV10mZ00mRvz1910WV3z2es5KLg9dyP2oL///+Y3YyXBMF7AAAAC3RSTlMANHubyP9Q8BDgICxpogoAAAEoSURBVHgBfNAlQERBFIXhi9NwiLg0HDoOae3i1guuBYce6AHrGetY296RaRSctffO6F9WvnGCCtv4v+5KMpXdycmWZnXdPWavsQZV01cYGqmQNQ3mxufno+a2s1J4G/iUtYZg6RWdR/zly9jQAk52TL9gY5vJY/eaObId5wy21BTnEhsH44wPdnWPTxd/bfabEiIKP2MvfwS/J4R4h5/r/1wLv2dkDsHWwLB5NtuZZynDxU2U4+J5KnFxkGpdHKJ2F4ep18URYhdziqd+Y30KcRv/ElX4Rki9KPwk8+tfYfVVBQAMhTDUNg6wjQLO/e3uG4mnfbieho8hLAgqUoKEohxQTChFFDLboH86aEE0MNof8BB6AC5gD9AEcgFs4B6ygGogKmgOkhxbBE1DHolywwAAAABJRU5ErkJggg==",
    ":hide:":"https://app.seesaw.me/static/images/shortcut-images/expand_shortcut@3x.png",
    ":like:":"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAD0AAAA2BAMAAACGi4wZAAAAKlBMVEVHcEz/P8/7O9f5OtT7Otb6O9f7O9f6Otf5Otf6O9b7Otb3N9f7Otf7O9egoZBWAAAADnRSTlMAEEMwkOD/pGDw0CDAe02+wYwAAAE4SURBVHgBtdKBRjxRFAbw7+7+/2IzDLBK2JYQYZEIqDdI2ACSna9aG4EALCi9wApQZCEYgAgFAyAw9DaNe+xtus05gn5gzOce95xz8Uuu31+vffeieHtI8kj+3sxIPuao2aKXTQH3QW8yQNCl4CTHBgVHIW7PuHCXMHhY5Lv8UjAYp/FxERfoUHEqeUmN73eZqgNUlqg6Q2WFqjEq19TlAK6oewcwpO4SAA33QIuG47/PHWkPmIZXAAXt+ZSkueAd6lIA/0nzASW092+/H3PBU58/U5EB5gVOIObG64A+gSyFSIzyRgfTkHfU4Qk3V28nVq3jUsA4LgWU48LFLezhu3/xZmO3rMkGiLXrV3zDT10GF2iyScHxAE1cQbGPZsnMx4fQvPjJpFCV5HkPutaQT7CsjWCLW/sEH2G9TZ4vZk8AAAAASUVORK5CYII=",
    ":comment:":"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAD0AAAA3BAMAAABN11+8AAAALVBMVEVHcEwvLy8zMzMvLy8zMzMyMjIyMjIzMzMzMzMzMzMyMjI1NTUyMjIzMzMzMzO1NFQ+AAAAD3RSTlMAIEAQgLDA/+CcWzBw8NAsv1FeAAABQUlEQVR4AWJABYxKDDgBs0pYORBUZK7GKi0DYJwuAVoLwzCOP/fiTmJ1jboICXfPuEecd8i3gjsUrOCuidX1irt7z3M98o5//R35tJFcXS/L+ZC8EjPSbxeQbzW+vk3SSrw5jmQJk4fDL0lep87tc6TUmIvDSDFxzL5OdOvgQFJJOEawRWo92ZfmUtXbmdHZi7W6hvEqZvS2WoB/xNQFRHIugGDi0iKE9WQYWS9GPOtVfvzJjzf/4fu8a1ifRhTrJgSxfoxwjvXs8SFq97//7ASmHcebPeABQ6reDVtG9vNQn6FBB/YCvbquP/86cKDotXAV8amydq4S5azXwqsTKYtkeBcp5TQfll5ywxp8C/XhslgJO09pTsMlGRpyjyGr0bEdav23sVhW9QSb/0K1LCufgfV+HeNb+kVwWcYkgEsGAG8KLdjAFJdHAAAAAElFTkSuQmCC"
}


# print(base64.decode(seesaw_icons[':comment:'], 'utf-8'))

for shortcut, img in seesaw_icons.items():
    print(shortcut, img)

    img_data = requests.get(img).content if not img.startswith('data:') else base64.b64decode(img.split('png;base64,')[1])
    with open(f"../icons/{shortcut.strip(':')}.png", 'wb') as img_file:
        img_file.write(img_data)