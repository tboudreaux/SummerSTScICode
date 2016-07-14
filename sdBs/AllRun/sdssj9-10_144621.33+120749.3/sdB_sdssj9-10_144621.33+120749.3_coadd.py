from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[221.588875,12.130361],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj9-10_144621.33+120749.3/sdB_sdssj9-10_144621.33+120749.3_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj9-10_144621.33+120749.3/sdB_sdssj9-10_144621.33+120749.3_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
