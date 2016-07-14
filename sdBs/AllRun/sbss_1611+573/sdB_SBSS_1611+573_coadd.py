from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[243.132542,57.247581],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SBSS_1611+573/sdB_SBSS_1611+573_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SBSS_1611+573/sdB_SBSS_1611+573_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
