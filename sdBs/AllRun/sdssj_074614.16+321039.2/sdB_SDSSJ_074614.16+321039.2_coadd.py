from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[116.559,32.177556],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_074614.16+321039.2/sdB_SDSSJ_074614.16+321039.2_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_074614.16+321039.2/sdB_SDSSJ_074614.16+321039.2_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
