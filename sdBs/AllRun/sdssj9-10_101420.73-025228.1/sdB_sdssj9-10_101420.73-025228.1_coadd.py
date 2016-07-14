from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[153.586375,-2.874472],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj9-10_101420.73-025228.1/sdB_sdssj9-10_101420.73-025228.1_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj9-10_101420.73-025228.1/sdB_sdssj9-10_101420.73-025228.1_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
