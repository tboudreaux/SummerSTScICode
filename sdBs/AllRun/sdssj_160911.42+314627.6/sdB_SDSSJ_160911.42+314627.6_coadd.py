from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[242.297583,31.774333],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_160911.42+314627.6/sdB_SDSSJ_160911.42+314627.6_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_160911.42+314627.6/sdB_SDSSJ_160911.42+314627.6_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
