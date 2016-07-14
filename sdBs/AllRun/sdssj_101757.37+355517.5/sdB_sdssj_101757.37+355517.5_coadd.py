from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[154.489042,35.921528],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_101757.37+355517.5/sdB_sdssj_101757.37+355517.5_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_101757.37+355517.5/sdB_sdssj_101757.37+355517.5_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
