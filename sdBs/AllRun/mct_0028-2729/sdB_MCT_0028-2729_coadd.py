from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[7.803917,-27.21505],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_MCT_0028-2729/sdB_MCT_0028-2729_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_MCT_0028-2729/sdB_MCT_0028-2729_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
