from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[354.638583,47.495639],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_233833.26+472944.3/sdB_SDSSJ_233833.26+472944.3_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_233833.26+472944.3/sdB_SDSSJ_233833.26+472944.3_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
