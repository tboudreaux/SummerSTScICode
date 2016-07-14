from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[65.654875,-54.147292],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_galex_j04226-5408/sdB_galex_j04226-5408_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_galex_j04226-5408/sdB_galex_j04226-5408_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
