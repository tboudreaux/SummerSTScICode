from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[53.069708,-2.550489],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_galex_j03322-0233/sdB_galex_j03322-0233_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_galex_j03322-0233/sdB_galex_j03322-0233_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()