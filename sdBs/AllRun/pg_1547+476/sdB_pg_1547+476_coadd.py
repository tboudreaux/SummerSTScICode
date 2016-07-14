from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[237.180708,47.493425],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1547+476/sdB_pg_1547+476_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1547+476/sdB_pg_1547+476_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()