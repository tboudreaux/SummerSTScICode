from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[31.196292,27.484594],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_galex_j02047+2729/sdB_galex_j02047+2729_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_galex_j02047+2729/sdB_galex_j02047+2729_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
