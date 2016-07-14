from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[134.712833,2.170492],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_galex_j08588+0210/sdB_galex_j08588+0210_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_galex_j08588+0210/sdB_galex_j08588+0210_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
