from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[321.499042,-11.095925],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_galex_j21259-1105/sdB_galex_j21259-1105_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_galex_j21259-1105/sdB_galex_j21259-1105_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
