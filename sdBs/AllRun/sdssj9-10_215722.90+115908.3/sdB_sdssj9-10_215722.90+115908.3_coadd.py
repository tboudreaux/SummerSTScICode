from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[329.345417,11.985639],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj9-10_215722.90+115908.3/sdB_sdssj9-10_215722.90+115908.3_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj9-10_215722.90+115908.3/sdB_sdssj9-10_215722.90+115908.3_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
