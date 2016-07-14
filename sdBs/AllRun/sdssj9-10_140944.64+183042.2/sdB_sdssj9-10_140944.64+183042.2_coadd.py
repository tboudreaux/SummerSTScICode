from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[212.436,18.511722],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj9-10_140944.64+183042.2/sdB_sdssj9-10_140944.64+183042.2_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj9-10_140944.64+183042.2/sdB_sdssj9-10_140944.64+183042.2_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
