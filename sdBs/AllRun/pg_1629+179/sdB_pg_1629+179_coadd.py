from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[248.051167,17.888725],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1629+179/sdB_pg_1629+179_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1629+179/sdB_pg_1629+179_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
