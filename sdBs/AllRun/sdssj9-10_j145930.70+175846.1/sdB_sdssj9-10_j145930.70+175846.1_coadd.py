from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[224.877917,17.979472],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj9-10_j145930.70+175846.1/sdB_sdssj9-10_j145930.70+175846.1_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj9-10_j145930.70+175846.1/sdB_sdssj9-10_j145930.70+175846.1_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
