from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[325.479042,82.193081],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_HS_2143+8157/sdB_HS_2143+8157_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_HS_2143+8157/sdB_HS_2143+8157_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
