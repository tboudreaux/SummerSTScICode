from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[248.580708,34.712444],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj9-10_163419.37+344244.8/sdB_sdssj9-10_163419.37+344244.8_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj9-10_163419.37+344244.8/sdB_sdssj9-10_163419.37+344244.8_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
